from django import forms


## Formulario de añadir partidos ##
class PartidoForm(forms.Form):
    nombre = forms.CharField()
