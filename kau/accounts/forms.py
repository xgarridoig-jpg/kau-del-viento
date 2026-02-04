from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
