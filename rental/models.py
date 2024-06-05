from django.db import models

class UAV(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    rental_date = models.DateTimeField()

    def __str__(self):
        return f"Rental of {self.uav} on {self.rental_date}"

class InventoryItem(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    rented_to = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.status}"
