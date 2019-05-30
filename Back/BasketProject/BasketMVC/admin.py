from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = "Panel de Administrador"


@admin.register(jugador)
class jugadorAdmin(admin.ModelAdmin):
    list_display = ('equipo','nombre','apellido1','apellido2')
    ordering = ('equipo',)
    search_fields=('nombre','equipo')


@admin.register(equipo)
class equipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields=('nombre',)

@admin.register(partido)
class partidoAdmin(admin.ModelAdmin):
    list_display = ('equipo1','equipo2','fase','fecha')
    ordering = ('fase',)


