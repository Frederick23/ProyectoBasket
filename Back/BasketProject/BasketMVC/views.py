from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola y bienvenido al index")