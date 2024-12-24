from django.contrib import admin

from unfold.admin import ModelAdmin

from payme.models import PaymeTransactions
from click_up.models import ClickTransaction


admin.site.unregister(PaymeTransactions)
admin.site.unregister(ClickTransaction)


@admin.register(PaymeTransactions)
class PaymeTransactionsAdmin(ModelAdmin):
    """
    Admin for PaymeTransactions with display, search, and filter options.
    """
    list_display = ['transaction_id', 'state', 'created_at']
    search_fields = ['transaction_id']
    list_filter = ['state']


@admin.register(ClickTransaction)
class ClickTransactionAdmin(ModelAdmin):
    """
    Admin for ClickTransaction with display, search, and filter options.
    """
    list_display = ['transaction_id', 'account_id', 'state', 'created_at']
    search_fields = ['transaction_id']
    list_filter = ['state']
