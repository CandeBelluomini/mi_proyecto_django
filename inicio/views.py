from django.shortcuts import render
from django.http import HttpResponse


# def inicio(request):
#     return HttpResponse("Hola Mundo")

def inicio(request):
    
    return render(request, "inicio/inicio.html")

def prueba_bucle(request):
    
    numeros = list(range(1, 11))
    
    return render(request, "inicio/prueba_bucle.html", {"datos": numeros})
