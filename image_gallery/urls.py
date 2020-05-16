from django.urls import path
from .views import gallery


"""
 This module contains all the possible urls configured for image_gallery app.
"""

urlpatterns = [
    path('', gallery, name='gallery')
]
