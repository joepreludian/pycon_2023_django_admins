from django.db import models


class Model(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    model = models.ForeignKey('car.Model', on_delete=models.CASCADE, related_name='vehicles')
    plate = models.CharField(max_length=8)
    mileage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.model} - {self.plate}"
