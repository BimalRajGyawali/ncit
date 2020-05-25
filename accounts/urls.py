from django.urls import path
from .views import CollectRollView,VerifyEmailView, \
    RegisterAjaxView, StudentHomeView, LogInAjaxView, \
    LogInView, RegisterView


urlpatterns = [
    path('roll-ajax/', CollectRollView.as_view(), name='collect_roll'),
    path('verify-ajax/', VerifyEmailView.as_view(), name='verify_email'),
    path('register-ajax/', RegisterAjaxView.as_view(), name='register_ajax'),
    path('login-ajax/', LogInAjaxView.as_view(), name='login_ajax'),
    path('student-home/', StudentHomeView.as_view(), name='student_home'),
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')

]