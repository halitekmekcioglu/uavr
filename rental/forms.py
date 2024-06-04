from django import forms
from .models import UAV, Rental

class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['uav', 'rental_date']
