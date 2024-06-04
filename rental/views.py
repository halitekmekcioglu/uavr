from rest_framework import viewsets, permissions
from .models import UAV, Rental
from .serializers import UAVSerializer, RentalSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import render
from django.contrib.auth.views import LoginView


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import UAVForm, RentalForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    # Redirect to a desired URL after logout
    return redirect('login.html')  # Redirect to the login page after logout

@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def logout(request):
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

# Similarly, create views for deleting, updating, and listing UAVs and rental records



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







