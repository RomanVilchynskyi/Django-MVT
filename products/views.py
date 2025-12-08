from django.shortcuts import render

# Create your views here.

def index(request):

    # load data from db
    # checks etc...
    return render(request, 'products/index.html')

def detail(request, product_id):
    return render(request, 'products/detail.html', {'product_id': product_id})

def about(request, product_id):
    return render(request, 'products/about.html', {'product_id': product_id})