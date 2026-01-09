from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price_per_day']
    search_fields = ['brand', 'model']
    list_filter = ['year']

admin.site.register(Car, CarAdmin)
