import math
from django.shortcuts import render
from math import *

# Create your views here.

def index(request):
    context = {
        'titulo': 'Operaciones matemáticas',
    }
    return render(request, 'propuesto/operaciones.html', context)


def solucion(request):
    operacion = request.POST['operaciones']
    numero1 = int(request.POST['numero1'])
    numero2 = int(request.POST['numero2'])
    resultado = 0

    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2
    elif operacion == 'division':
        resultado = numero1 / numero2


    context = {
        'numero1' : numero1,
        'numero2' : numero2,
        'operacion' : operacion,
        'resultado' : resultado,
    }
    return render(request, 'propuesto/resultado.html', context)


def volumen(request):
    context = {
        'titulo': 'CÁLCULO DEL VOLUMEN DE UN CILINDRO',
    }
    return render(request, 'propuesto/volumen.html', context)


def resultadovolumen(request):
    altura = int(request.POST['altura'])
    diametro = int(request.POST['diametro'])
    resultado = pi * math.pow(diametro/2, 2) * altura
    context = {
        'resultado' : resultado,
    }
    return render(request, 'propuesto/resultadovolumen.html', context)