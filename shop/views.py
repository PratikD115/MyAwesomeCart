from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    nslides = n//4 + ceil(n/4 - n//4)
    params = {'slides': nslides, 'range': range(1, nslides), 'product': products, }
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('contact shop')


def tracker(request):
    return HttpResponse('tracker shop')


def search(request):
    return HttpResponse('search shop')


def productView(request):
    return HttpResponse('productView shop')


def checkOut(request):
    return HttpResponse('checkout shop')