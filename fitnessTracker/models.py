from django.db import models

# Create your models here.
class Measurements(models.Model):
    weight = models.FloatField() # in kg
    waist  = models.FloatField() # in inches
