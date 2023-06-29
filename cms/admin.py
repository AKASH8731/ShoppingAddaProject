from django.contrib import admin
from cms.models import *


class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone", "address")
    search_fields = ("title", "email", "phone", "address")
    list_filter = ("email", "phone")


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ("heading", "sub_heading", "image", "status")
    search_fields = ("heading", "sub_heading")
    list_filter = ("heading", "sub_heading")


admin.site.register(Slider, SliderAdmin)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", "description", "author",
                    "date_time", "status")
    search_fields = ("title", "author")
    list_filter = ("author",)


admin.site.register(Blog, BlogAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "status")
    search_fields = ("question", "answer")
    list_filter = ("question", "answer")


admin.site.register(FAQs, FAQsAdmin)


class About_UsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "designation")
    list_filter = ("designation",)


admin.site.register(About_Us, About_UsAdmin)


class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")
    search_fields = ("name", "email", "phone")
    list_filter = ("email", "phone")


admin.site.register(ContactUs, Contact_UsAdmin)
