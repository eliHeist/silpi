from django.contrib import admin
from accounts.admin import user_admin

from products.models import Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

user_admin.register(Category)

# @user_admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

user_admin.register(Product, ProductAdmin)
    