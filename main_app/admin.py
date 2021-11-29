from django.contrib import admin

# Register your models here.

from django.contrib import admin
# import your models here
from .models import Trip, Photo

# Register your models here
admin.site.register(Trip)
admin.site.register(Photo)