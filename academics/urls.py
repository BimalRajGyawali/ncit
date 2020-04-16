from django.urls import path
from .views import program, home, facility, scholarship, test


urlpatterns = [
    path('', home, name='home'),
    path('programs/<int:code>', program, name='programs'),
    path('facilities/', facility, name='facility'),
    path('scholarships/', scholarship, name='scholarship'),
]
