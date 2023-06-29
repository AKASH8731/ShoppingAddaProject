from django.contrib import admin
from order.models import *
# Register your models here.


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ("date_time", "address", "mobile", "payment", "status")
    search_fields = ("date_time", "address", "mobile", "payment")
    list_filter = ("mobile", "payment")
    inlines = (OrderDetailsInline,)


admin.site.register(Order, OrderAdmin)


# class OrderDetailsAdmin(admin.ModelAdmin):
#     list_display = ("order", "product", "quantity", "price")
#     search_fields = ("order", "product", "quantity", "price")
#     list_filter = ("order", "product",)


# admin.site.register(OrderDetails, OrderDetailsAdmin)
