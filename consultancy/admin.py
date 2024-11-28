from django.contrib import admin

from consultancy.models import ConsultancyProject

from accounts.admin import user_admin
from unfold.admin import ModelAdmin

@admin.register(ConsultancyProject)
class ConsultancyProjectAdminClass(ModelAdmin):
    pass
# Register your models here.

user_admin.register(ConsultancyProject)