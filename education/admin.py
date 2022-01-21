from django.contrib import admin
from .models import Education, Certificate

class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ("create_date", "update_date")

admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, EducationAdmin)