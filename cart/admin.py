from django.contrib import admin
from django.forms import inlineformset_factory
from cart.models import Order, OrderItem, CartItem
from unfold.admin import ModelAdmin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Number of empty forms to display

@admin.register(Order)
class OrderAdminClass(ModelAdmin):
    inlines = [OrderItemInline]
    
@admin.register(CartItem)
class CartItemAdminClass(ModelAdmin):
    pass

