from django.contrib import admin
from django.forms import inlineformset_factory
from cart.models import Order, OrderItem, CartItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Number of empty forms to display

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]




# Register your models here.
admin.site.register(CartItem)

