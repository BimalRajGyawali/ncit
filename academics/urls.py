from django.urls import path
from .views import program, home


urlpatterns = [
    path('', home, name='home'),
    path('programs/<int:code>', program, name='programs'),
]
