from django.contrib import admin

from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    Admin Interface for Order
    """
    list_display = (
        "id",
        "customer_name",
        "address",
        "total_cost",
        "payment_method",
        "is_paid"
    )
    list_filter = ("is_paid", "payment_method",)
    search_fields = ("id", "customer_name", "address", "payment_method")


admin.site.register(Order, OrderAdmin)
