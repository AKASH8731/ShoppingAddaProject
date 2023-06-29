from django.contrib import admin, messages
from product.models import *


def active_status(modelAdmin, request, queryset):
    queryset.update(status=True)
    messages.success(request, "You Marked Selected Record As Active")


def inactive_status(modelAdmin, request, queryset):
    queryset.update(status=False)
    messages.warning(request, "You Marked Selected Record As InActive")


"""inlines - TabularInline StackedInline at the time of product is added we will get space/option to add/delete image on the same page"""


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "product_category", "name",
                    "price", "description", "status")
    search_fields = ("id", "name", "price")
    list_filter = ("id", "product_category", "price")
    inlines = (ProductImageInline,)
    actions = (active_status, inactive_status)


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status", "show_on_homepage")


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ("name", "status")


admin.site.register(ProductVariation, ProductVariationAdmin)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ("name", "status")


admin.site.register(ProductTag, ProductTagAdmin)


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ("product", "image")


# admin.site.register(ProductImage, ProductImageAdmin)
