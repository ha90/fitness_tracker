from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# main page
def index(request):
    template = loader.get_template('fitnessTracker/index.html')
    return render(request, 'fitnessTracker/index.html')

# measurement page
def measurements(request):
    return HttpResponse("Coming Soon...")

    
