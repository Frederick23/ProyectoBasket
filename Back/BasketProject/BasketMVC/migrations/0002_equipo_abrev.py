# Generated by Django 2.2 on 2019-06-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketMVC', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='abrev',
            field=models.CharField(default='VAC', max_length=100, verbose_name='Abreviatura'),
        ),
    ]
