from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # List view configuration
    list_display = ('user_id', 'name', 'level', 'occupation', 'age', 'withdraw_method', 'account_balance')
    list_filter = ('level', 'withdraw_method', 'age')
    search_fields = ('name', 'occupation', 'user_id')
    
    # Detail view configuration
    fieldsets = (
        ("User Information", {
            'fields': ('user_id', 'name', 'level', 'occupation', 'age')
        }),
        ("Account Information", {
            'fields': ('withdraw_method', 'withdraw_account_id', 'account_balance', 'bank_no', 'ufsc')
        }),
    )
    
    readonly_fields = ('user_id',)  # Make user_id read-only, as it is generated automatically

    # Optional: Configure default ordering
    ordering = ('name',)

