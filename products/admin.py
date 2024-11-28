from django.contrib import admin
from accounts.admin import user_admin

from products.models import Category, Product
from unfold.admin import ModelAdmin

# Register your models here.
user_admin.register(Category)

# @user_admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

user_admin.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdminClass(ModelAdmin):
    pass

@admin.register(Product)
class ProductAdminClass(ModelAdmin):
    pass


    