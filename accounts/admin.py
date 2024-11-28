from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from unfold.admin import ModelAdmin

from accounts.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

class UserAdminArea(admin.AdminSite):
    site_header = 'SLK INITIATIVES LTD'
    site_title = 'SLK INITIATIVES LTD'


user_admin = UserAdminArea(name='UserAdmin')