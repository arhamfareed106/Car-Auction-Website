from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

from django.urls import path

from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the start index.")

def start(request):
    return HttpResponse("Hello, world. You're at the start start.")

def start_view(request):
    return JsonResponse({"message": "Hello, world. You're at the start start."})

