from typing import Type
from django.db import models

# Create your models here.
class Trip(models.Model): 
  name = models.CharField(max_length=100)
  # type = models.CharField(max_length=1, default= 's',choices=Type)
  distance = models.IntegerField()
  description = models.TextField(max_length=500)
  topspeed = models.IntegerField()