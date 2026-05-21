from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class InicioSesion(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
class FormularioCreacion(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nombre de usuario",
            "email": "Email"
        }
        help_texts = {
            "username": ""
        }
        
class EditarPerfil(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ["first_name","last_name", "email"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Email",
        }
        
class FormularioCambioContraseña(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Vieja", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Contraseña Nueva", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirmar Contraseña Nueva", widget=forms.PasswordInput)