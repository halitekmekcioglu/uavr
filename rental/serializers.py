from rest_framework import serializers
from django.contrib.auth.models import User  # Import the User model from auth module
from .models import UAV, Rental

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use the User model directly
        fields = ['id', 'username', 'email']

class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Use the UserSerializer defined above
    uav = UAVSerializer(read_only=True)
    uav_id = serializers.PrimaryKeyRelatedField(
        queryset=UAV.objects.all(), source='uav', write_only=True)
    
    class Meta:
        model = Rental
        fields = '__all__'
