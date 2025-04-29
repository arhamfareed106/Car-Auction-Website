

from django.http import HttpResponse
from django.views import View
from django.urls import path
from django.http import JsonResponse
from django.shortcuts import render

from car.start.views import index, start, start_view



urlpatterns = [
    path('', index, name='index'),
    path('start/', start, name='start'),
    path('start_view/', start_view, name='start_view'),
    path('start_view/<int:id>/', start_view, name='start_view_with_id'),
    path('start_view/<int:id>/<str:name>/', start_view, name='start_view_with_id_and_name'),
    path('start_view/<int:id>/<str:name>/<str:age>/', start_view, name='start_view_with_id_name_and_age'),
    path('start_view/<int:id>/<str:name>/<str:age>/<str:email>/', start_view, name='start_view_with_id_name_age_and_email'),
]
