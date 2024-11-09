from django.contrib import admin

from unfold.admin import ModelAdmin

from payme.models import PaymeTransactions

admin.site.unregister(PaymeTransactions)


@admin.register(PaymeTransactions)
class PaymeTransactionsAdmin(ModelAdmin):
    """
    Admin for PaymeTransactions with display, search, and filter options.
    """
    list_display = ['transaction_id', 'state', 'created_at']
    search_fields = ['transaction_id']
    list_filter = ['state']
