from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from cars.models import Car

# Create your models here.

class CarRental(models.Model):

    STATUS_CHOICES = (
        ('active', 'Активна'),
        ('finished', 'Завершена'),
        ('canceled', 'Скасована'),
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='rentals'
    )

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)

    start_date = models.DateField()
    end_date = models.DateField()

    total_price = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Дата початку не може бути пізніше дати завершення")

        overlapping = CarRental.objects.filter(
            car=self.car,
            status='active',
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("Автомобіль вже орендований у цей період")

    def save(self, *args, **kwargs):
        self.full_clean() 
        days = (self.end_date - self.start_date).days + 1
        self.total_price = days * self.car.price_per_day
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.car} ({self.start_date} → {self.end_date})"