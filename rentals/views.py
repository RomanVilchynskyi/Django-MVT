from django.shortcuts import render, redirect

from cars.models import Car
from rentals.models import CarRental
from .forms import CarRentalForm
from django.contrib import messages

def rentals_list(request):
    rentals = CarRental.objects.all()
    return render(request, "rentals/index.html", {"rentals": rentals})


def rent_create(request):
    car_id = request.GET.get('car')
    car = None

    if car_id:
        car = Car.objects.filter(id=car_id).first()

    if request.method == "POST":
        form = CarRentalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Car has been rent successfully")
            return redirect('cars_list')
    else:
        form = CarRentalForm(initial={'car': car})

    return render(
        request,
        "rentals/create.html",
        {
            "form": form,
            "selected_car": car
        }
    )

