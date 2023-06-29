from django.contrib import admin
from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "mobile",)
    search_fields = ("__user_first_name ", "__user_first_name", "mobile")


admin.site.register(UserProfile, UserProfileAdmin)
