# Generated by Django 2.2.1 on 2019-06-06 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0014_remove_stats_equipo_tiempo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='TIEMPO',
        ),
    ]
