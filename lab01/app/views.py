from django.http import HttpResponse

def suma(request, numero_1, numero_2):
    total = "La suma de " + str(numero_1) + " + " + str(numero_2) + " = " + str(numero_1 + numero_2)
    return HttpResponse(total)

def resta(request, numero_1, numero_2):
    total = "La resta de " + str(numero_1) + " - " + str(numero_2) + " = " + str(numero_1 - numero_2)
    return HttpResponse(total)

def multiplicacion(request, numero_1, numero_2):
    total = "La multiplicación de " + str(numero_1) + " * " + str(numero_2) + " = " + str(numero_1 * numero_2)
    return HttpResponse(total)