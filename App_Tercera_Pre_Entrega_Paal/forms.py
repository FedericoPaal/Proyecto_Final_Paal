from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *

class Novedades_Formulario(forms.ModelForm):
    
    class Meta:
        model = Novedad
        fields = '__all__'

class Libros_Formulario(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = '__all__'


class Merchandising_Formulario(forms.ModelForm):
    
    class Meta:
        model = Merchandising
        fields = '__all__'  

class Consultas_Formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    consulta = forms.CharField(label="Consulta", widget=forms.Textarea)

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    

class Avatar_Formulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)


class Cliente_Formulario(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields = ("nombre", "apellido", "email")


class Staff_Formulario(forms.ModelForm):
    
    class Meta:
        model=Staff
        fields = ("nombre", "apellido", "email")