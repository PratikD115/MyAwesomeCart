from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse('about shop')


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