from django.shortcuts import render, redirect, get_object_or_404
from .models import Car

TEST_CARS = [
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price_per_day": 1500,
        "description": "Комфортний седан бізнес-класу.",
        "image": "https://i.imgur.com/Py1qK2j.jpeg"
    },
    {
        "id": 2,
        "brand": "BMW",
        "model": "X5",
        "year": 2019,
        "price_per_day": 2500,
        "description": "Преміум позашляховик, повний привід.",
        "image": "https://i.imgur.com/JmYrB2f.jpeg"
    },
    {
        "id": 3,
        "brand": "Honda",
        "model": "Civic",
        "year": 2018,
        "price_per_day": 1100,
        "description": "Економний і надійний автомобіль.",
        "image": "https://i.imgur.com/b5nC5Rh.jpeg"
    }
]


def cars_index(request):
    # cars = Car.objects.all()
    return render(request, "cars/index.html", {"cars": TEST_CARS})


def cars_detail(request, car_id):
    # car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/detail.html", {"car": [car_id - 1]})


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


# def cars_delete(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     car.delete()
#     return redirect("/cars")
