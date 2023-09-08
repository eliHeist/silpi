from django.db import models

from products.models import Product

class CartItem(models.Model):
    session_key = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.product.name} * {self.quantity}'
