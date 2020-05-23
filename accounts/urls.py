from django.urls import path
from .views import collect_roll,verify_email, \
    register_ajax, student_home, login_ajax, \
    login, register


urlpatterns = [
    path('roll-ajax/', collect_roll, name='collect_roll'),
    path('verify-ajax/', verify_email, name='verify_email'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('student-home/', student_home, name='student_home'),
    path('login/', login, name='login'),
    path('register/', register, name='register')

]