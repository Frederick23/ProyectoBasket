# Generated by Django 2.2 on 2019-05-31 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0002_auto_20190530_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='AS',
            field=models.IntegerField(default=0, verbose_name='AS'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='DES',
            field=models.IntegerField(default=0, verbose_name='DES'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='F',
            field=models.IntegerField(default=0, verbose_name='F'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='FTO',
            field=models.IntegerField(default=0, verbose_name='F+'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='I_TC2',
            field=models.IntegerField(default=0, verbose_name='2PI'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='I_TC3',
            field=models.IntegerField(default=0, verbose_name='3PI'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='I_TL',
            field=models.IntegerField(default=0, verbose_name='TLI'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='PER',
            field=models.IntegerField(default=0, verbose_name='PER'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='REBD',
            field=models.IntegerField(default=0, verbose_name='REBD'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='REBO',
            field=models.IntegerField(default=0, verbose_name='REBO'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='REBT',
            field=models.IntegerField(default=0, verbose_name='REBT'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='REC',
            field=models.IntegerField(default=0, verbose_name='REC'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TAP',
            field=models.IntegerField(default=0, verbose_name='TAP'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TC2',
            field=models.IntegerField(default=0, verbose_name='TC2'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TC2_P',
            field=models.IntegerField(default=0, verbose_name='TC2%'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TC3',
            field=models.IntegerField(default=0, verbose_name='TC3'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TC3_P',
            field=models.IntegerField(default=0, verbose_name='TC3%'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TC_P',
            field=models.IntegerField(default=0, verbose_name='TC%'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TL',
            field=models.IntegerField(default=0, verbose_name='TL'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='TL_P',
            field=models.IntegerField(default=0, verbose_name='TL%'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='puntos_contra',
            field=models.IntegerField(default=0, verbose_name='Pts Contra'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='puntos_favor',
            field=models.IntegerField(default=0, verbose_name='Pts Favor'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='AS',
            field=models.IntegerField(default=0, verbose_name='AS'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='AS_p',
            field=models.FloatField(default=0, verbose_name='A/P'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='DES',
            field=models.IntegerField(default=0, verbose_name='DES'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='F',
            field=models.IntegerField(default=0, verbose_name='F'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='FTO',
            field=models.IntegerField(default=0, verbose_name='F+'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='I_TC2',
            field=models.IntegerField(default=0, verbose_name='2PI'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='I_TC3',
            field=models.IntegerField(default=0, verbose_name='3PI'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='I_TL',
            field=models.IntegerField(default=0, verbose_name='TLI'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='PER',
            field=models.IntegerField(default=0, verbose_name='PER'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REBD',
            field=models.IntegerField(default=0, verbose_name='REBD'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REBO',
            field=models.IntegerField(default=0, verbose_name='REBO'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REBT',
            field=models.IntegerField(default=0, verbose_name='REBT'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REB_p',
            field=models.FloatField(default=0, verbose_name='REB/P'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REC',
            field=models.IntegerField(default=0, verbose_name='REC'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='REC_p',
            field=models.FloatField(default=0, verbose_name='REC/P'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TAP',
            field=models.IntegerField(default=0, verbose_name='TAP'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TAP_p',
            field=models.FloatField(default=0, verbose_name='T/P'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TC2',
            field=models.IntegerField(default=0, verbose_name='TC2'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TC2_P',
            field=models.IntegerField(default=0, verbose_name='TC2%'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TC3',
            field=models.IntegerField(default=0, verbose_name='TC3'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TC3_P',
            field=models.IntegerField(default=0, verbose_name='TC3%'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TC_P',
            field=models.IntegerField(default=0, verbose_name='TC%'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 5, 31, 9, 44, 36, 786057), verbose_name='Tiempo'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TL',
            field=models.IntegerField(default=0, verbose_name='TL'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='TL_P',
            field=models.IntegerField(default=0, verbose_name='TL%'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='p_p',
            field=models.FloatField(default=0, verbose_name='p/p'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='partidos',
            field=models.IntegerField(default=0, verbose_name='NºPartidos'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='pts',
            field=models.IntegerField(default=0, verbose_name='Pts'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='AS',
            field=models.IntegerField(default=0, verbose_name='AS'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='DES',
            field=models.IntegerField(default=0, verbose_name='DES'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='EFI',
            field=models.FloatField(default=0, verbose_name='EFI'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='F',
            field=models.IntegerField(default=0, verbose_name='F'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='FTO',
            field=models.IntegerField(default=0, verbose_name='F+'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='I_TC2',
            field=models.IntegerField(default=0, verbose_name='2PI'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='I_TC3',
            field=models.IntegerField(default=0, verbose_name='3PI'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='I_TL',
            field=models.IntegerField(default=0, verbose_name='TLI'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='I_ZONA',
            field=models.IntegerField(default=0, verbose_name='ZONAI'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='PER',
            field=models.IntegerField(default=0, verbose_name='PER'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='POS',
            field=models.FloatField(default=0, verbose_name='POS'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='P_POS',
            field=models.FloatField(default=0, verbose_name='P/POS'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='REBD',
            field=models.IntegerField(default=0, verbose_name='REBD'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='REBO',
            field=models.IntegerField(default=0, verbose_name='REBO'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='REBT',
            field=models.IntegerField(default=0, verbose_name='REBT'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='REC',
            field=models.IntegerField(default=0, verbose_name='REC'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='TAP',
            field=models.IntegerField(default=0, verbose_name='TAP'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='TC2',
            field=models.IntegerField(default=0, verbose_name='TC2'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='TC3',
            field=models.IntegerField(default=0, verbose_name='TC3'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 5, 31, 9, 44, 36, 786057), verbose_name='Tiempo'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='TL',
            field=models.IntegerField(default=0, verbose_name='TL'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='VENT',
            field=models.IntegerField(default=0, verbose_name='VENT'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='ZONA',
            field=models.IntegerField(default=0, verbose_name='ZONA'),
        ),
        migrations.AddField(
            model_name='stats_equipo',
            name='pts',
            field=models.IntegerField(default=0, verbose_name='Pts'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='AS',
            field=models.IntegerField(default=0, verbose_name='AS'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='DES',
            field=models.IntegerField(default=0, verbose_name='DES'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='EFI',
            field=models.FloatField(default=0, verbose_name='EFI'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='F',
            field=models.IntegerField(default=0, verbose_name='F'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='FTO',
            field=models.IntegerField(default=0, verbose_name='F+'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='I_TC2',
            field=models.IntegerField(default=0, verbose_name='2PI'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='I_TC3',
            field=models.IntegerField(default=0, verbose_name='3PI'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='I_TL',
            field=models.IntegerField(default=0, verbose_name='TLI'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='PER',
            field=models.IntegerField(default=0, verbose_name='PER'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='REBD',
            field=models.IntegerField(default=0, verbose_name='REBD'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='REBO',
            field=models.IntegerField(default=0, verbose_name='REBO'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='REBT',
            field=models.IntegerField(default=0, verbose_name='REBT'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='REC',
            field=models.IntegerField(default=0, verbose_name='REC'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='TAP',
            field=models.IntegerField(default=0, verbose_name='TAP'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='TC2',
            field=models.IntegerField(default=0, verbose_name='TC2'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='TC3',
            field=models.IntegerField(default=0, verbose_name='TC3'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 5, 31, 9, 44, 36, 786057), verbose_name='Tiempo'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='TL',
            field=models.IntegerField(default=0, verbose_name='TL'),
        ),
        migrations.AddField(
            model_name='stats_jugador',
            name='pts',
            field=models.IntegerField(default=0, verbose_name='Pts'),
        ),
    ]