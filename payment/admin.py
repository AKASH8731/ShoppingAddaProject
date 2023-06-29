from django.contrib import admin
from payment.models import *

# Register your models here.


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("order", "transaction_id", "status")
    search_fields = ("id", "transaction_id", "status")
    list_filter = ("transaction_id", "status")


admin.site.register(Payments, PaymentsAdmin)
