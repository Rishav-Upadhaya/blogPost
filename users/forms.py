from django import forms
# from .models import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class userForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=500)
#     password = forms.CharField(max_length=500)
#     password2 = forms.CharField(max_length=500)

# class userForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']