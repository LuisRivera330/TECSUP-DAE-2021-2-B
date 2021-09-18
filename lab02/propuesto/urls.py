from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'propuesto'

urlpatterns = [

    path('', views.index, name='index'),
    path('solucion',views.solucion,name='solucion'),
    path('volumen', views.volumen, name='volumen'),
    path('solucion/volumen',views.resultadovolumen,name='resultadovolumen'),
]