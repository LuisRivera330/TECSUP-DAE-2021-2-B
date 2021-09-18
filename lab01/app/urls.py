from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/app/sumar/18/19
    path('sumar/<int:numero_1>/<int:numero_2>', views.suma, name='suma'),
    # ex: localhost:8080/app/restar/18/19
    path('restar/<int:numero_1>/<int:numero_2>', views.resta, name='resta'),
    # ex: localhost:8080/app/sumar/18/19
    path('multiplicar/<int:numero_1>/<int:numero_2>', views.multiplicacion, name='multiplicacion'),

]