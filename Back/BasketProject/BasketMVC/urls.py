from django.urls import path
from BasketMVC import views


urlpatterns = [

    ## Login ##

    ## Inicio ##
    path('', views.index, name = 'index'),

    ## Ver jugador ##
    path('mostrar_jugadores', views.Mostrar, name = 'Mostrar'),

    ## Ver listado de equipos ##
    path('upload', views.upload_partido, name='upload_partido'),

    ## Ver un equipo ##
    path('formpartido', views.formulario_partido, name="formulario_partido")

    ## Ver un partido ##

    ## Ver un listado de partidos ##

    ## Agregar un partido ##

]

