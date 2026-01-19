from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price_per_day = models.PositiveIntegerField()  
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars_photos/', blank=True, null=True)  

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
  

