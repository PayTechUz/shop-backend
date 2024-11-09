from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from unfold.admin import ModelAdmin

from order.models import Order

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    """
    Admin for User model with custom extensions.
    """


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    """
    Admin for Group model with custom extensions.
    """


class OrderAdmin(ModelAdmin):
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
