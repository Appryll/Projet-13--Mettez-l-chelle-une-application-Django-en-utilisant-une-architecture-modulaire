from django.contrib import admin
from .models import Letting
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "street", "city", "state", "zip_code", "country_iso_code")
    ordering = ("city",)
    list_filter = ("zip_code", "city",)


class LettingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "address")
    ordering = ("title",)
    list_filter = ("address",)


admin.site.register(Letting, LettingAdmin)
admin.site.register(Address, AddressAdmin)
