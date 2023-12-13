from django.contrib import admin

from accounts.models import User

# Register your models here.
admin.site.register(User)

class UserAdminArea(admin.AdminSite):
    site_header = 'SLK INITIATIVES LTD'
    site_title = 'SLK INITIATIVES LTD'


user_admin = UserAdminArea(name='UserAdmin')