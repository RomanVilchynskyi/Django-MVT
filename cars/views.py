from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from cars.forms import CarForm
from favorites.favorites import get_count_of_favorite_cars, get_favorite_cars
from .models import Car

def cars_index(request):
    cars = Car.objects.all()

    return render(request, "cars/index.html", {"cars": cars, "fav_count": get_count_of_favorite_cars(request), "fav_cars": get_favorite_cars(request)})

def cars_list(request):
    cars = Car.objects.all()
    return render(request, "cars/adminIndex.html", {"cars": cars})



def cars_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, "cars/detail.html", {"car": car})

def cars_create(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)  # ← ВАЖЛИВО
        if form.is_valid():
            form.save()
            messages.success(request, f"Car has been created successfully")
            return redirect('cars_list')  # ← ІМʼЯ маршруту
    else:
        form = CarForm()
    return render(request, "cars/create.html", {"form": form})

def cars_edit(request, pk):
    # шукаємо барбера за id
    car = get_object_or_404(Car, pk=pk)

    if request.method == "POST":
        # створюємо форму з даними з запиту та існуючого барбера
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            # зберігаємо зміни в базу
            car = form.save()
            messages.success(request, f"Car has been edited successfully")
            return redirect('cars_list')
    else:
        # створюємо форму з даними знайденого барбера
        form = CarForm(instance=car)
    return render(request, "cars/edit.html", {"form": form})


def cars_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    messages.success(request, f"Car has been deleted successfully")
    return redirect("/cars")

def save(self, *args, **kwargs):
    days = (self.end_date - self.start_date).days + 1
    self.total_price = days * self.car.price_per_day
    super().save(*args, **kwargs)