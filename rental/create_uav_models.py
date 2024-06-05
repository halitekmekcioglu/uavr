# create_uav_models.py

from django.utils import timezone
from .models import UAV  

def create_uav_models():
    uav_models = [
        {"brand": "Brand 1", "model": "Model 1", "weight": 10.5, "category": "Category 1"},
        {"brand": "Brand 2", "model": "Model 2", "weight": 20.5, "category": "Category 2"},
        # Add more UAV models as needed
    ]

    for uav_data in uav_models:
        uav = UAV.objects.create(**uav_data)
        uav.save()

if __name__ == "__main__":
    create_uav_models()
