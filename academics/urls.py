from django.urls import path
from .views import program, home, facility, scholarship, contact_us

"""
 This module contains all the possible urls configured for users_app.
"""
urlpatterns = [
    path('', home, name='home'),
    path('programs/<int:code>', program, name='programs'),
    path('facilities/', facility, name='facility'),
    path('scholarships/', scholarship, name='scholarship'),
    path('contact-us/', contact_us, name="contact_us"),
]
