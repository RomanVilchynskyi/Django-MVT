from django.shortcuts import render, redirect, get_object_or_404
from .models import Car


def cars_index(request):
    cars = Car.objects.all()
    return render(request, "cars/index.html", {"cars": cars})


def cars_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, "cars/detail.html", {"car": car})


# def cars_create(request):
#     if request.method == "POST":
#         Car.objects.create(
#             brand=request.POST["brand"],
#             model=request.POST["model"],
#             year=request.POST["year"],
#             price_per_day=request.POST["price_per_day"],
#             description=request.POST.get("description", ""),
#             image=request.POST.get("image", "")
#         )
#         return redirect("/cars")

#     return render(request, "cars/create.html")


# def cars_edit(request, car_id):
#     car = get_object_or_404(Car, id=car_id)

#     if request.method == "POST":
#         car.brand = request.POST["brand"]
#         car.model = request.POST["model"]
#         car.year = request.POST["year"]
#         car.price_per_day = request.POST["price_per_day"]
#         car.description = request.POST.get("description", "")
#         car.image = request.POST.get("image", "")
#         car.save()

#         return redirect("/cars")

#     return render(request, "cars/edit.html", {"car": car})


def cars_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect("/cars")
