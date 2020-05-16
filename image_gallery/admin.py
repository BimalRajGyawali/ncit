from django.contrib import admin
from .models import Image


"""
   Image Model is registered to admin site.
"""

admin.site.register(Image)