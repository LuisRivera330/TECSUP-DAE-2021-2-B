from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Prestamos
from .serializers import PrestamosSerilizer

@api_view(['GET'])
def index(request):
    return Response({'mensaje': 'Api rest de prestamos'})

@api_view(['GET'])
def prestamos(request):
        lstprestamos = Prestamos.objects.all()
        serPres = PrestamosSerilizer(lstprestamos, many=True)
        return Response(serPres.data)