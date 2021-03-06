# IMPORTS
from django.urls import path
from . import views



urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('trips/', views.trips_index, name='trips_index'),
  path('trips/<int:trip_id>/', views.trips_detail, name='trips_detail'),
  path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
  path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
  path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('trips/<int:trip_id>/add_photo/', views.add_photo, name='add_photo'),
]