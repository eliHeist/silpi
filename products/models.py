from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    thumbnail = models.ImageField()
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    details = RichTextField()
    price = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    