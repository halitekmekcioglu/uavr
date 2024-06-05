# views.py

from rest_framework import viewsets, permissions
from .models import UAV, Rental
from .serializers import UAVSerializer, RentalSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout

from .forms import UAVForm, RentalForm

class UAVViewSet(viewsets.ModelViewSet):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout

def home(request):
    return render(request, 'login.html')

def base(request):
    return render(request, 'base.html')

@login_required
def profile(request):
    uav_form = UAVForm()
    rental_form = RentalForm()
    return render(request, 'profile.html', {'uav_form': uav_form, 'rental_form': rental_form})

def add_uav(request):
    if request.method == 'POST':
        form = UAVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UAVForm()
    return render(request, 'add_uav.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def index(request):
    return render(request, 'index.html')
