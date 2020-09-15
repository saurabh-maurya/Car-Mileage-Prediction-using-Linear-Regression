from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('predictMileage', views.predictMileage, name='predictMileage'),
]
