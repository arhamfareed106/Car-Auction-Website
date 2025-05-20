

from django.http import HttpResponse
from django.views import View
from django.urls import path
from django.http import JsonResponse
from django.shortcuts import render

from car.start.views import index, start, start_view  # Ensure start_view is defined in views.py



urlpatterns = [
    path('', index, name='index'),
    path('start/', start, name='start'),
    path('start_view/', start_view, name='start_view'),

]
