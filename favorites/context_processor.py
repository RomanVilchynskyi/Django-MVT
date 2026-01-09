from favorites.favorites import get_count_of_favorite_cars


def favorite_cars_count(request):
    return { 'fav_count': get_count_of_favorite_cars(request) }