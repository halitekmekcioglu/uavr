from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental.views import UAVViewSet, RentalViewSet


router = DefaultRouter()
router.register(r'uavs', UAVViewSet)
router.register(r'rentals', RentalViewSet)





from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('rental.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


