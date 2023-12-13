from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='posts/')
    details = RichTextField()
    
    date_posted = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    