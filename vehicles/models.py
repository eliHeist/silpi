from django.db import models

# Create your models here.
CONDITIONS = (
    ('Brand New', 'Brand New'),
    ('Used', 'Used'),
)

ACTIONS = (
    ('Hire', 'Hire'),
    ('Purchase', 'Purchase'),
    ('Hire & Purchase', 'Hire & Purchase'),
)

class Vehicle(models.Model):
    image = models.ImageField(upload_to='vehicles/')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    condition = models.CharField(max_length=20, choices=CONDITIONS)
    more_details = models.TextField(null=True, blank=True)
    actions = models.CharField(max_length=20, choices=ACTIONS)
    
    def __str__(self) -> str:
        return f'{self.make}. {self.model}'

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.vehicle.model

class VehicleOrderRequest(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f'Order for {self.vehicle.make}. {self.vehicle.model}'