from django.db import models



class jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False)
    apellido1 = models.CharField('Primer Apellido', max_length=30, blank=False)
    apellido2 = models.CharField('Segundo Apellido', max_length=30, blank=False)
    fecha_nac = models.DateField(blank=False)

class equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30)
    sede = models.CharField('Dirección')

class partido(models.Model):

    # Constantes de partido
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

    id = models.AutoField(primary_key=True)
    equipo1 = models.ForeignKey(equipo, on_delete=models.PROTECT)
    equipo2 = models.ForeignKey(equipo, on_delete=models.PROTECT)
    fecha = models.DateField(blank=False)
    localizacion = models.CharField(max_length=30)
    fase = models.CharField(choices=FASES, blank=False)

    cuarto1 = models.CharField(blank=False, max_length=5)
    cuarto2 = models.CharField(blank=False, max_length=5)
    cuarto3 = models.CharField(blank=False, max_length=5)
    cuarto4 = models.CharField(blank=False, max_length=5)
    tiempos_extra = models.CharField(blank=False, max_length=5)
    tanteo_final = models.CharField(blank=False, max_length=7)

    jugadores = models.ManyToManyField(jugador, related_name="Jugadores")
