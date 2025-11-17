from rest_framework import views
from rest_framework import response

from payme import Payme
from click_up import ClickUp

from backend import settings
from order.serializer import OrderSerializer


payme = Payme(
    payme_id=settings.PAYME_ID,
    license_api_key=settings.PAYTECH_API_KEY
)

click_up = ClickUp(
    service_id=settings.CLICK_SERVICE_ID,
    merchant_id=settings.CLICK_MERCHANT_ID
)


class OrderCreate(views.APIView):
    """
    API endpoint for creating an order.
    """
    serializer_class = OrderSerializer

    def post(self, request):
        """
        Create a new order.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        result = {
            "order": serializer.data
        }

        if serializer.data["payment_method"] == "payme":
            payment_link = payme.initializer.generate_pay_link(
                id=serializer.data["id"],
                amount=serializer.data["total_cost"],
                return_url="https://uzum.uz"
            )
            result["payment_link"] = payment_link

        elif serializer.data["payment_method"] == "click":
            payment_link = click_up.initializer.generate_pay_link(
                id=serializer.data["id"],
                amount=serializer.data["total_cost"],
                return_url="https://uzum.uz"
            )
            result["payment_link"] = payment_link

        return response.Response(result)
