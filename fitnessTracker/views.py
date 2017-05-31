from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# main page
def index(request):
    return render(request, 'fitnessTracker/index.html')

# measurement page
def measurements(request):
    return render(request, 'fitnessTracker/measurements.html')

    
