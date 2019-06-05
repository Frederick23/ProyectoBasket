from django import forms


## Formulario de añadir partidos ##
class PartidoForm(forms.Form):
    equipo1 = forms.CharField()
    equipo2 = forms.CharField()

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
    file = forms.FileField()

