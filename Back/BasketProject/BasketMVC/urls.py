from django.urls import path
from django.conf.urls import url
from BasketMVC import views


urlpatterns = [
    ## Vacio ##
    path('', views.index, name='index'),

    ## Inicio ##
    path('index', views.index, name = 'index'),

    ## Ver jugador ##
    path('jugador', views.mostrar_jugador, name = 'Jugador'),

    ## Ver jugadores ##
    path('mostrar_jugadores', views.Mostrar, name = 'Mostrar'),

    ## Ver listado de equipos ##
    path('equipos', views.mostrar_Equipos, name='Equipos'),

    ## Ver un equipo ##
    path('equipo', views.mostrar_equipo, name='Equipo'),
    url(r'^equipo/$', views.mostrar_equipo, name='Equipo'),

    ## Ver un partido ##
    path('partido', views.mostrar_partido, name='Partido'),

    ## Ver un listado de partidos ##
    path('partidos', views.mostrar_Partidos, name='Partidos'),

    ## Agregar un partido ##
    path('upload', views.formulario_partido, name='upload_partido'),

]

