# IMPORTS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Trip
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class TripCreate(CreateView):
  model = Trip
  fields = '__all__'
  success_url = '/trips/'

class TripUpdate(UpdateView):
  model = Trip
  # Let's disallow the renaming of a Trip by excluding the name field!
  fields = ['name', 'type', 'distance', 'description', 'topspeed']

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'