from django import forms
from .models import Message
class ContactUsForm(forms.ModelForm):
    class Meta :
        fields = ['email','name','message']
        model = Message