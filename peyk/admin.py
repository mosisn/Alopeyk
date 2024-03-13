from django.contrib.admin import register, ModelAdmin
from .models import Account, Order

@register(Account)
class AccountAdmin(ModelAdmin):
    pass

@register(Order)
class OrderAdmin(ModelAdmin):
    pass
