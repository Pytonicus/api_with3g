from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("create_date", "update_date")

admin.site.register(Project, ProjectAdmin)