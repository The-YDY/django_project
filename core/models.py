from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    first_registration = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=100)
    engine_size = models.IntegerField()
    power = models.IntegerField()
    gearbox = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    doors = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    vehicle_extras = models.TextField()
    vehicle_description = models.TextField(blank=False)
    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=100)
    contact_mobile_phone = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=255)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('car_details', args=[self.id])
        