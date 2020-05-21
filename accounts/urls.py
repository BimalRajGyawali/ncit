from django.urls import path
from .views import LogInView, RegisterView, collect_roll
urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('roll/', collect_roll)
]