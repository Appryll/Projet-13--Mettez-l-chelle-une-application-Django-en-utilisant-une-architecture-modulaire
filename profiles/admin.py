from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "favorite_city")
    ordering = ("user",)
    list_filter = ("user", "favorite_city",)


admin.site.register(Profile, ProfileAdmin)
