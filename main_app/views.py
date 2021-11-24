from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Rider!</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def trips_index(request):
  return render(request, 'trips/index.html', { 'trips': trips })

def home(request):
  return render(request, 'home.html')

class Trip:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, distance, description, topspeed):
    self.name = name
    self.distance = distance
    self.description = description
    self.topspeed = topspeed

trips = [
  Trip('Bushwick Cruise', 84, 'Late night, super cold. The bridges looked beautiful though.', 53 ),
  Trip('Jersey Motorsports', 213, 'Jersey was a blast, tires were cold at first but got em to temps and the Striple was sticking like glue in the corners.', 202),
  Trip('Long Island Woods', 55, 'Trails were nice and clear, no big obstacles, got to feel like a rally driver for the afternoon.', 37),
]