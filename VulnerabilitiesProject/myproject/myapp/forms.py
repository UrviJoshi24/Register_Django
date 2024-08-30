# myapp/forms.py
from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'contact_number', 'email_id', 'gender', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
