from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("Hola Mundo desde Django!")

def saludar_con_etiqueta(request):
     return HttpResponse ("<h1>Hola Mundo desde Django!</h1>")

def saludar_con_nombre(request, nombre:str):
    nombre = nombre.capitalize()
    return HttpResponse(f"<h1>Hola {nombre} desde Django!</h1>")

def index(request):
     context = {"año":2024}
     return render(request, "core/index.html", context)

