from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ConsultancyProject(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    client_name = models.CharField(max_length=100, null=True, blank=True)
    project_date = models.DateField()
    services_offered = models.CharField(max_length=200)
    project_duration = models.CharField(max_length=50)
    project_location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title