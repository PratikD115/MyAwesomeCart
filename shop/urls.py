from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='shopIndex'),
    path('about/', views.about, name='shopAbout'),
    path('contact/', views.contact, name='shopContact'),
    path('tracker/', views.tracker, name='shopTracker'),
    path('search/', views.search, name='shopSearch'),
    path('productview/', views.productView, name='shopProductView'),
    path('checkout/', views.checkOut, name='shopCheckOut')
]
