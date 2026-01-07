from django.shortcuts import redirect, render

from cars.models import Car
from favorites.favorites import add_car_to_favorites, get_favorite_cars, remove_car_from_favorites


def index(request):
    cars = Car.objects.all()
    favoriteIds = get_favorite_cars(request)

    cars = [car for car in cars if car.id in favoriteIds]
    return render(request, "favorites/index.html", {"cars": cars})

def add_car(request, car_id, return_url):
    add_car_to_favorites(request, car_id)
    return redirect(return_url)

def remove_car(request, car_id, return_url):
    remove_car_from_favorites(request, car_id)
    return redirect(return_url)