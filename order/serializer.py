from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Order model serializer
    """
    class Meta:
        """
        Define the fields and their corresponding model fields
        """
        model = Order
        fields = "__all__"
