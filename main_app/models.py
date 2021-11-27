# IMPORTS
from typing import Type
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


TYPE = (('Street', 'Street'),('Offroad', 'Offroad'),('Track', 'Track'))

# Create your models here.
class Trip(models.Model): 
  # date = models.DateField()
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=150, default=TYPE[0][0],choices=TYPE)
  distance = models.IntegerField()
  description = models.TextField(max_length=500)
  topspeed = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('trips_detail', kwargs={'trip_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=250)
  trip = models.OneToOneField(Trip, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for trip_id: {self.trip_id} @{self.url}"
  
  # def __str__(self):
  #   return self.date