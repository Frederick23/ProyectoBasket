from django.http import HttpResponse
from django.shortcuts import render
from BasketMVC.models import jugador


def index(request):
    return HttpResponse("Hola y bienvenido al index")


def Mostrar(request):
    return render(request, 'tabla.html', {'jugadores': jugador.objects.all()})