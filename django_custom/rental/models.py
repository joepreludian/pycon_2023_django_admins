from django.db import models


class Rent(models.Model):
    vehicle = models.ForeignKey('car.Vehicle', on_delete=models.SET_NULL, null=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='rents')

    def __str__(self):
        return f'Rent for {self.user} - ${self.vehicle}'
