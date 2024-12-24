from click_up.views import ClickWebhook
from click_up.models import ClickTransaction

from order.models import Order


# pylint: disable=E1101
class ClickWebhookAPIView(ClickWebhook):
    """
    A view to handle Click Webhook API calls.
    This view will handle all the Click Webhook API events.
    """
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )
        order = Order.objects.get(id=transaction.account_id)
        order.is_paid = True
        order.save()

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )

        if transaction.state == ClickTransaction.CANCELLED:
            order = Order.objects.get(id=transaction.account_id)
            order.is_paid = False
            order.save()
