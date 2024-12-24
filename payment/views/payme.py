from payme.types import response
from payme.views import PaymeWebHookAPIView
from payme.models import PaymeTransactions

from order.models import Order


# pylint: disable=E1101
class PaymeCallBackAPIView(PaymeWebHookAPIView):
    """
    A view to handle Payme Webhook API calls.
    This view will handle all the Payme Webhook API events.
    """
    def check_perform_transaction(self, params):
        account = self.fetch_account(params)
        self.validate_amount(account, params.get('amount'))

        result = response.CheckPerformTransaction(allow=True)

        # you can use dynamic parameters it simple example that's why hardcoded
        item = response.Item(
            discount=10000,
            title="Помидоры",
            price=505000,
            count=1,
            code="00702001001000001",
            units=241092,
            vat_percent=15,
            package_code="123456"
        )
        result.add_item(item)
        return result.as_resp()

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        transaction = PaymeTransactions.get_by_transaction_id(
            transaction_id=params["id"]
        )

        order = Order.objects.get(id=transaction.account_id)
        order.is_paid = True
        order.save()

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        transaction = PaymeTransactions.get_by_transaction_id(
            transaction_id=params["id"]
        )

        if transaction.state == PaymeTransactions.CANCELED:
            order = Order.objects.get(id=transaction.account_id)
            order.is_paid = False
            order.save()
