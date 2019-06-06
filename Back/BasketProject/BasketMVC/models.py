from django.db import models
import datetime



class equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30)
    sede = models.CharField('Dirección', max_length=100)

    # Estadísticas acumuladas

    TC_P = models.IntegerField('TC%',default=0)
    TC2 = models.IntegerField('TC2',default=0)
    I_TC2 = models.IntegerField('2PI',default=0)
    TC2_P = models.IntegerField('TC2%',default=0)

    TC3 = models.IntegerField('TC3',default=0)
    I_TC3 = models.IntegerField('3PI',default=0)
    TC3_P = models.IntegerField('TC3%',default=0)

    TL = models.IntegerField('TL',default=0)
    I_TL = models.IntegerField('TLI',default=0)
    TL_P = models.IntegerField('TL%',default=0)

    AS = models.IntegerField('AS',default=0)
    TAP = models.IntegerField('TAP',default=0)
    REBO = models.IntegerField('REBO',default=0)
    REBD = models.IntegerField('REBD',default=0)
    REBT = models.IntegerField('REBT',default=0)
    REC = models.IntegerField('REC',default=0)
    DES = models.IntegerField('DES',default=0)
    F = models.IntegerField('F',default=0)
    PER = models.IntegerField('PER',default=0)
    FTO = models.IntegerField('F+',default=0)

class jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False)
    apellido1 = models.CharField('Primer Apellido', max_length=30, blank=False)
    apellido2 = models.CharField('Segundo Apellido', max_length=30, blank=False)
    fecha_nac = models.DateField(blank=False)
    dorsal = models.CharField('Dorsal', max_length=3, blank=False, default="0")
    equipo = models.ForeignKey(equipo, on_delete=models.PROTECT, related_name="Equipo", default=1)

    # Estadísticas acumuladas
    partidos = models.IntegerField('NºPartidos', default=0)
    pts = models.IntegerField('Pts', default=0)
    p_p = models.FloatField('p/p', default=0)
    TC_P = models.IntegerField('TC%', default=0)

    TC2 = models.IntegerField('TC2', default=0)
    I_TC2 = models.IntegerField('2PI', default=0)
    TC2_P = models.IntegerField('TC2%', default=0)

    TC3 = models.IntegerField('TC3', default=0)
    I_TC3 = models.IntegerField('3PI', default=0)
    TC3_P = models.IntegerField('TC3%', default=0)

    TL = models.IntegerField('TL', default=0)
    I_TL = models.IntegerField('TLI', default=0)
    TL_P = models.IntegerField('TL%', default=0)

    AS = models.IntegerField('AS', default=0)
    AS_p = models.FloatField('A/P', default=0)
    TAP = models.IntegerField('TAP', default=0)
    TAP_p = models.FloatField('T/P', default=0)

    REBO = models.IntegerField('REBO', default=0)
    REBD = models.IntegerField('REBD', default=0)
    REBT = models.IntegerField('REBT', default=0)
    REB_p = models.FloatField('REB/P', default=0)

    REC = models.IntegerField('REC', default=0)
    REC_p = models.FloatField('REC/P', default=0)
    DES = models.IntegerField('DES', default=0)
    F = models.IntegerField('F', default=0)
    PER = models.IntegerField('PER', default=0)
    FTO = models.IntegerField('F+', default=0)






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
    fecha = models.CharField(max_length=12,blank=False)
    localizacion = models.CharField(max_length=30)
    fase = models.CharField(choices=FASES, blank=False, max_length=100)

    cuarto1 = models.CharField(blank=False, max_length=5)
    cuarto2 = models.CharField(blank=False, max_length=5)
    cuarto3 = models.CharField(blank=False, max_length=5)
    cuarto4 = models.CharField(blank=False, max_length=5)
    tiempos_extra = models.CharField(blank=False, max_length=5)
    tanteo_final = models.CharField(blank=False, max_length=7)



class stats_jugador(models.Model):
    id_jugador = models.ForeignKey(jugador, on_delete=models.PROTECT)
    id_partido = models.ForeignKey(partido, on_delete=models.PROTECT)

    pts = models.IntegerField('Pts', default=0)
    TC2 = models.IntegerField('TC2', default=0)
    I_TC2 = models.IntegerField('2PI', default=0)
    TC3 = models.IntegerField('TC3', default=0)
    I_TC3 = models.IntegerField('3PI', default=0)
    TL = models.IntegerField('TL', default=0)
    I_TL = models.IntegerField('TLI', default=0)

    AS = models.IntegerField('AS', default=0)
    TAP = models.IntegerField('TAP', default=0)
    REBO = models.IntegerField('REBO', default=0)
    REBD = models.IntegerField('REBD', default=0)
    REBT = models.IntegerField('REBT', default=0)
    REC = models.IntegerField('REC', default=0)
    DES = models.IntegerField('DES', default=0)
    F = models.IntegerField('F', default=0)
    PER = models.IntegerField('PER', default=0)
    FTO = models.IntegerField('F+', default=0)
    TIEMPO = models.CharField('Tiempo', max_length=10)
    EFI = models.FloatField('EFI',default=0)

    class Meta:
        unique_together = ('id_jugador', 'id_partido')

class stats_equipo(models.Model):
    id_equipo = models.ForeignKey(equipo, on_delete=models.PROTECT)
    id_partido = models.ForeignKey(partido, on_delete=models.PROTECT)

    # Total del equipo
    pts = models.IntegerField('Pts', default=0)
    TC2 = models.IntegerField('TC2', default=0)
    I_TC2 = models.IntegerField('2PI', default=0)
    TC3 = models.IntegerField('TC3', default=0)
    I_TC3 = models.IntegerField('3PI', default=0)
    TL = models.IntegerField('TL', default=0)
    I_TL = models.IntegerField('TLI', default=0)

    AS = models.IntegerField('AS', default=0)
    TAP = models.IntegerField('TAP', default=0)
    REBO = models.IntegerField('REBO', default=0)
    REBD = models.IntegerField('REBD', default=0)
    REBT = models.IntegerField('REBT', default=0)
    REC = models.IntegerField('REC', default=0)
    DES = models.IntegerField('DES', default=0)
    F = models.IntegerField('F', default=0)
    PER = models.IntegerField('PER', default=0)
    FTO = models.IntegerField('F+', default=0)
    EFI = models.FloatField('EFI',default=0)

    # Del equipo en conjunto
    POS = models.FloatField('POS',default=0)
    P_POS =models.FloatField('P/POS',default=0)
    ZONA = models.IntegerField('ZONA',default=0)
    I_ZONA = models.IntegerField('ZONAI',default=0)
    VENT = models.IntegerField('VENT',default=0)

    class Meta:
        unique_together = ('id_equipo', 'id_partido')
