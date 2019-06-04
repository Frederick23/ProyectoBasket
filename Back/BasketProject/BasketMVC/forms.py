from django import forms


## Formulario de añadir partidos ##
class PartidoForm(forms.Form):
    equipo1 = forms.CharField()
    equipo2 = forms.CharField()
    fase = forms.CharField()
    file = forms.FileField()

