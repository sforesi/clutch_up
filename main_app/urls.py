from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for trip index
  path('trips/', views.trips_index, name='trips_index')
]