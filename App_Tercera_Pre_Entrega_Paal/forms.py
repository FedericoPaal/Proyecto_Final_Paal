from django import forms

class Novedades_Formulario(forms.Form):
    
    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    precio = forms.CharField(max_length=40)


class Libros_Formulario(forms.Form):
    
    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    precio = forms.CharField(max_length=40)


class Merchandising_Formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    precio = forms.CharField(max_length=40)


class Consultas_Formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    consulta = forms.CharField(max_length=1000)