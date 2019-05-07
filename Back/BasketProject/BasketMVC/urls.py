from django.urls import path
from BasketMVC import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mostrar_jugadores', views.Mostrar, name = 'Mostrar'),
    path('upload', views.upload_partido, name='upload_partido'),
    path('formpartido', views.formulario_partido, name="formulario_partido")
]

