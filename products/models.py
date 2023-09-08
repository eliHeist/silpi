from django.db import models

# Create your models here.
class Category(models.Model):
    thumbnail = models.ImageField()
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    details = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name