from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from .forms import UAVForm, RentalForm, InventoryItemForm
from .models import UAV, Rental
from .serializers import UAVSerializer, RentalSerializer

from django.shortcuts import render
from .models import InventoryItem

from django.shortcuts import render
from .models import InventoryItem
from django.contrib.auth.decorators import login_required

@login_required
def list_inventory(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'list_inventory.html', {'inventory_items': inventory_items})

@login_required
def manage_inventory(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_inventory')  # Redirect to a success page
    else:
        form = InventoryItemForm()
    return render(request, 'manage_inventory.html', {'form': form})

@login_required
def inventory_management(request):
    # Your view logic here
    return render(request, 'inventory_management.html')


@login_required
def rent_page(request):
    rentable_uavs = UAV.objects.filter(rentable=True)
    return render(request, 'rent_page.html', {'rentable_uavs': rentable_uavs})

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
    return redirect('login')

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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def index(request):
    return render(request, 'index.html')
