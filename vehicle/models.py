from django.db import models
from django.core.validators import RegexValidator


class Vehicle(models.Model):
    VEHICLE_TYPE = [('Two', 'Two Wheelar'), ('Three', 'Three Wheelar'), ('Four', 'Four Wheelar')]
    alphnum = RegexValidator(
        r'^[0-9a-zA-Z]*$',
        'Only letters and numbers are allowed.'
    )
    
    vehicle_number = models.CharField(validators=[alphnum], unique=True, max_length=30)
    vehicle_type = models.CharField(choices=VEHICLE_TYPE, max_length=10)
    vehicle_model = models.CharField(max_length=30)
    vehicle_description = models.TextField(max_length=100)
