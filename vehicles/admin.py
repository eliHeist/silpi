from django.contrib import admin

from vehicles.models import Vehicle
from accounts.admin import user_admin

# Register your models here.
admin.site.register(Vehicle)

user_admin.register(Vehicle)