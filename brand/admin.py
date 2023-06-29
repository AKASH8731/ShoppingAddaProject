from django.contrib import admin
from brand.models import *
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    search_fields = ("name",)
    list_filter = ("status",)


admin.site.register(Brand, BrandAdmin)
