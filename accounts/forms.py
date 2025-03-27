from django import forms
from .models import MyUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['phone_number', 'email', 'first_name', 'last_name']
    
