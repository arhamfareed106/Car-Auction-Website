from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

from django.urls import path

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    return HttpResponse("Hello, world. You're at the start index.")

def start(request):
    return HttpResponse("Hello, world. You're at the start start.")

def start_message_view(request):
    return JsonResponse({"message": "Hello, world. You're at the start start."})


    # User signup view
    def signup_view(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  # Redirect to login page after successful signup
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    # User login view
    def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('index')  # Redirect to index page after successful login
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    # User logout view
    def logout_view(request):
        logout(request)
        return redirect('login')  # Redirect to login page after logout

    @login_required
    def protected_view(request):
        return HttpResponse("This is a protected view. You must be logged in to see this.")

    class ProtectedClassView(View):
        @method_decorator(login_required)
        def get(self, request, *args, **kwargs):
            return HttpResponse("This is a protected class-based view. You must be logged in to see this.")
        



def start_data_view(request, id=None, name=None, age=None, email=None):
    data = {
        "id": id,
        "name": name,
        "age": age,
        "email": email
    }
    return JsonResponse(data)






    # Car sell view
    def sell_car_view(request):
        if request.method == 'POST':
            car_data = {
                'make': request.POST.get('make'),
                'model': request.POST.get('model'),
                'year': request.POST.get('year'),
                'price': request.POST.get('price'),
                'description': request.POST.get('description'),
            }
            # Save car data to the database (this is a placeholder, replace with actual database logic)
            # Example: Car.objects.create(**car_data)
            return JsonResponse({"message": "Car listed for sale successfully!", "car_data": car_data})
        return render(request, 'sell_car.html')

    # Car buy view
    def buy_car_view(request):
        if request.method == 'GET':
            # Fetch available cars from the database (this is a placeholder, replace with actual database logic)
            # Example: cars = Car.objects.all()
            cars = [
                {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020, "price": 20000},
                {"id": 2, "make": "Honda", "model": "Civic", "year": 2019, "price": 18000},
            ]
            return JsonResponse({"available_cars": cars})
        return HttpResponse("Invalid request method.", status=405)

