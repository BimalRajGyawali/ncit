from django.urls import path
from .views import LogInView, RegisterView, collect_roll,\
    verify_email, register, student_home

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('roll/', collect_roll, name='collect_roll'),
    path('verify/', verify_email, name='verify_email'),
    path('register/', register, name='register'),
    path('student-home/', student_home, name='student_home')
]