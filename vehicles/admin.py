from django.contrib import admin

from vehicles.models import Vehicle
from accounts.admin import user_admin
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(Vehicle)
class VehicleAdminClass(ModelAdmin):
    pass