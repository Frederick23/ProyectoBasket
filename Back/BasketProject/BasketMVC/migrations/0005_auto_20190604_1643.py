# Generated by Django 2.2 on 2019-06-04 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0004_auto_20190531_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 4, 16, 43, 30, 4541), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='fecha',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='stats_equipo',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 4, 16, 43, 30, 4541), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='stats_jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 4, 16, 43, 30, 4541), verbose_name='Tiempo'),
        ),
    ]