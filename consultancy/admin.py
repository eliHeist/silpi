from django.contrib import admin

from consultancy.models import ConsultancyProject

from accounts.admin import user_admin

# Register your models here.
admin.site.register(ConsultancyProject)

user_admin.register(ConsultancyProject)