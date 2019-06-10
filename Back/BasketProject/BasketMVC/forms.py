from django import forms
from BasketMVC.models import equipo


## Formulario de añadir partidos ##
class PartidoForm(forms.Form):
    equipo1 = forms.ModelChoiceField(
        queryset = equipo.objects.values_list('nombre', flat=True)
    )

    equipo1.widget.attrs.update({'class': 'form-control'})
    equipo2 = forms.ModelChoiceField(
        queryset = equipo.objects.values_list('nombre', flat=True)
    )
    equipo2.widget.attrs.update({'class': 'form-control'})

    PFASE = 'Primera Fase'
    SFASE = 'Segunda Fase'
    FINAL = 'Fase Final'
    ASCENSO = 'Fase Ascenso'

    FASES = (
        (PFASE, 'Primera Fase'),
        (SFASE, 'Segunda Fase'),
        (FINAL, 'Fase Final'),
        (ASCENSO, 'Fase de Ascenso')
    )

    fase = forms.ChoiceField(choices=FASES)
    fase.widget.attrs.update({'class': 'form-control'})
    file = forms.FileField()
    file.widget.attrs.update({'class': 'form-control'})
