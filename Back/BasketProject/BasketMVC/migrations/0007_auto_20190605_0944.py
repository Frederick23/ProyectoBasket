# Generated by Django 2.2 on 2019-06-05 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0006_auto_20190604_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 5, 9, 44, 43, 457370), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='stats_equipo',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 5, 9, 44, 43, 472969), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='stats_jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 5, 9, 44, 43, 472969), verbose_name='Tiempo'),
        ),
    ]