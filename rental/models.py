from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class UAV(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=100)

class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(default=timezone.now)
    
