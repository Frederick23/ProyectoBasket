# Generated by Django 2.2.1 on 2019-06-06 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0011_auto_20190606_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 6, 19, 34, 18, 664029), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='stats_equipo',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 6, 19, 34, 18, 667060), verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='stats_jugador',
            name='TIEMPO',
            field=models.TimeField(default=datetime.datetime(2019, 6, 6, 19, 34, 18, 666042), verbose_name='Tiempo'),
        ),
    ]
