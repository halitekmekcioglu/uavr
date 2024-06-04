from rest_framework import serializers
from .models import UAV, Rental

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'auth.User'
        fields = ['id', 'username', 'email']

class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'yourappname.UAV'
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    uav = UAVSerializer(read_only=True)
    uav_id = serializers.PrimaryKeyRelatedField(
        queryset=UAV.objects.all(), source='uav', write_only=True)
    
    class Meta:
        model = 'yourappname.Rental'
        fields = '__all__'
