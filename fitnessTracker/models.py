from django.db import models

# measurement track database
class Measurements(models.Model):
    timestamp = models.IntegerField() # unix timestamp
    weight = models.FloatField() # in kg
    waist  = models.FloatField() # in inches

# food database
class Foods(models.Model):
    name = models.CharField(max_length=100)
    alternateNames = models.CharField(max_length=200)
    #foodType = models.CharField()
    calories = models.FloatField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fat = models.FloatField()

# exercise database   
class Exercises(models.Model):
    name = models.CharField(max_length=100)
    #todo

# workout track database    
# TODO

# diet track database
# TODO
