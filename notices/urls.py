from django.urls import path
from .views import notice, single_notice


"""
 This module contains all the possible urls configured for notices app.
"""

urlpatterns = [
    path('', notice, name='notices'),
    path('<str:heading>/', single_notice, name='notice')
]
