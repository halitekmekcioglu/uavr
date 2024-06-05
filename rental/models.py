from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class UAV(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_manage_uav_inventory", "Can manage UAV inventory"),
        ]


# Create a custom permission
content_type = ContentType.objects.get_for_model(User)  # Assuming you want to assign permission to User model


class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(default=timezone.now)
