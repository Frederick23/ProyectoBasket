from django.urls import path
from BasketMVC import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mostrar_jugadores', views.Mostrar, name = 'Mostrar'),
]

