from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('trips/', views.trips_index, name='trips_index'),
  path('trips/<int:trip_id>/', views.trips_detail, name='trips_detail'),
  path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
]