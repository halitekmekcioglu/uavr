# urls.py

from django.urls import path,include
from .views import  CustomLoginView, signup, profile, base, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base, name='base'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('accounts/logout/', logout, name='logout'),  # Add path to signup view
    path('accounts/signup/',  signup, name='signup'),  # Add path to signup view
    path('accounts/profile/', profile, name='profile'),  # Add path to signup view
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
