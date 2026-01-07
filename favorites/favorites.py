FAVORITE_CARS_KEY = 'favorite_cars'

def get_favorite_cars(request):
    return request.session.get(FAVORITE_CARS_KEY, [])

def get_count_of_favorite_cars(request):
    return len(get_favorite_cars(request))

def add_car_to_favorites(request, car_id):
    favoriteIds = get_favorite_cars(request)
    if car_id not in favoriteIds:
        favoriteIds.append(car_id)
        request.session[FAVORITE_CARS_KEY] = favoriteIds
    request.session.modified = True

def remove_car_from_favorites(request, car_id):
    favoriteIds = get_favorite_cars(request)
    if car_id in favoriteIds:
        favoriteIds.remove(car_id)
        request.session[FAVORITE_CARS_KEY] = favoriteIds
    request.session.modified = True