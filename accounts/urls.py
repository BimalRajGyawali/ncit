from django.urls import path
from .views import LogInView, RegisterView
urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup')
]