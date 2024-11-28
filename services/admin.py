from services.models import Service
from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(Service)
class ServiceAdminClass(ModelAdmin):
    pass