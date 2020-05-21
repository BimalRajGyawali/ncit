from django import forms
from .models import StudentLogin

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    roll = forms.IntegerField()

    class Meta:
        model = StudentLogin
        fields = ['roll', 'email', 'password', 'password1']



class StudentLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    roll = forms.IntegerField()

    class Meta:
        model = StudentLogin
        fields = ['roll', 'password']