from django.urls import path, include
from .views import CustomLoginView, signup, profile, base, logout_view,inventory_management
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import rent_page
from django.urls import path
from . import views
#from .views import inventory_management


urlpatterns = [
    path('', base, name='base'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('accounts/logout/', logout_view, name='logout'),  # Use custom logout view
    path('accounts/signup/', signup, name='signup'),  # Add path to signup view
    path('accounts/profile/', profile, name='profile'),  # Add path to profile view
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('rent/', rent_page, name='rent_page'),
    path('inventory/', views.inventory_management, name='inventory_management'),
    #path('inventory/', inventory_management, name='inventory_management'),

    path('inventory/list/', views.list_inventory, name='list_inventory'),
    path('inventory/manage/', views.manage_inventory, name='manage_inventory'),
    

]
