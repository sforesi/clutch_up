# IMPORTS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trip
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# VIEW DEFINITIONS
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
@login_required
def trips_index(request):
  trips = Trip.objects.filter(user=request.user)
  return render(request, 'trips/index.html', { 'trips': trips })

def home(request):
  return render(request, 'home.html')

@login_required
def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  return render(request, 'trips/detail.html', { 'trip': trip })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('trips_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class TripCreate(LoginRequiredMixin, CreateView):
  model = Trip
  fields = ['name', 'type', 'distance', 'description', 'topspeed']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)
  success_url = '/trips/'

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  # Let's disallow the renaming of a Trip by excluding the name field!
  fields = ['name', 'type', 'distance', 'description', 'topspeed']

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/trips/'