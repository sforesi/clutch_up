# IMPORTS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Trip

# VIEW DEFINITIONS
def home(request):
  return HttpResponse('<h1>Hello Rider!</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def home(request):
  return render(request, 'home.html')

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  return render(request, 'trips/detail.html', { 'trip': trip })
