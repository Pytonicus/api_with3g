from django.contrib import admin
from .models import Carreer

class CarreerAdmin(admin.ModelAdmin):
    readonly_fields = ("create_date", "update_date")

admin.site.register(Carreer,CarreerAdmin)
