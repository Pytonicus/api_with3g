from django.contrib import admin
from about.models import About, TechType, Tech

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ("create_date", "update_date")

admin.site.register(About, AboutAdmin)
admin.site.register(TechType, AboutAdmin)
admin.site.register(Tech, AboutAdmin)