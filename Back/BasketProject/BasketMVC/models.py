from django.db import models



class equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30)
    sede = models.CharField('Dirección', max_length=100)

class jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False)
    apellido1 = models.CharField('Primer Apellido', max_length=30, blank=False)
    apellido2 = models.CharField('Segundo Apellido', max_length=30, blank=False)
    fecha_nac = models.DateField(blank=False)
    dorsal = models.CharField('Dorsal', max_length=3, blank=False, default="0")
    equipo = models.ForeignKey(equipo, on_delete=models.PROTECT, related_name="Equipo", default=1)

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
    equipo1 = models.ForeignKey(equipo, on_delete=models.PROTECT, related_name="Local")
    equipo2 = models.ForeignKey(equipo, on_delete=models.PROTECT, related_name="Visitante")
    fecha = models.DateField(blank=False)
    localizacion = models.CharField(max_length=30)
    fase = models.CharField(choices=FASES, blank=False, max_length=100)

    cuarto1 = models.CharField(blank=False, max_length=5)
    cuarto2 = models.CharField(blank=False, max_length=5)
    cuarto3 = models.CharField(blank=False, max_length=5)
    cuarto4 = models.CharField(blank=False, max_length=5)
    tiempos_extra = models.CharField(blank=False, max_length=5)
    tanteo_final = models.CharField(blank=False, max_length=7)

    jugadores = models.ManyToManyField(jugador, related_name="Jugadores")

class stats_jugador(models.Model):
    id_jugador = models.ForeignKey(jugador, on_delete=models.PROTECT)
    id_partido = models.ForeignKey(partido, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('id_jugador', 'id_partido')

class stats_equipo(models.Model):
    id_equipo = models.ForeignKey(equipo, on_delete=models.PROTECT)
    id_partido = models.ForeignKey(partido, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('id_equipo', 'id_partido')
