from django import forms
from .models import UAV, Rental, InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['brand', 'model', 'weight', 'category', 'status', 'rented_to', 'from_date', 'to_date']

class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['uav', 'rental_date']
