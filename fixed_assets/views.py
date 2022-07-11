from django.utils import dateparse
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from authentication.authTokentodoapp import CsrfExemptSessionAuthentication, BasicAuthentication

from .serializers import *

# Create your views here.
class Ping(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request):
        return Response({'msg': 'Pong. API live'},status=status.HTTP_200_OK)
    
    
class ListUbicacion(generics.ListAPIView):
    
    serializer_class = UbicacionSerializer
    def get_queryset(self):
        queryset = Ubicacion.objects.all()
        return queryset
    

class ListArea(generics.ListAPIView):
    
    serializer_class = AreaSerializer
    def get_queryset(self):
        queryset = Area.objects.all()
        return queryset
    
    
class ListLinea(generics.ListAPIView):
    
    serializer_class = LineaSerializer
    def get_queryset(self):
        queryset = Linea.objects.all()
        return queryset
    
    
class ListStatusActivo(generics.ListAPIView):
    
    serializer_class = StatusActivoSerializer
    def get_queryset(self):
        queryset = StatusActivo.objects.all()
        return queryset
    
    
class ListDetailActivoFijo(generics.ListAPIView):
    
    serializer_class = ActivoFijoSerializer
    def get_queryset(self):
        a_f = self.request.query_params.get('consecutivo').upper()
        queryset = ActivoFijo.objects.filter(consecutivo=a_f)
        return queryset
    
    
class CreateActivoFijo(APIView):
    def post(self, request):
        ubicacion = int(request.data["ubicacion_id"])
        area = int(request.data["area_id"])
        linea = int(request.data["linea_id"])
        n_activo_sap = request.data["n_activo_sap"]
        n_pedimento = request.data["n_pedimento"]
        principal = request.data["principal"]
        descripcion = request.data["descripcion"]
        marca = request.data["marca"]
        modelo = request.data["modelo"]
        n_serie = request.data["n_serie"]
        id_adicional = request.data["id_adicional"] # no es un id, identificador adicional
        año = dateparse.parse_date(request.data["año"])
        pais_origen = request.data["pais_origen"]
        
        try:
            ubicacion = Ubicacion.objects.get(id=ubicacion)
            area = Area.objects.get(id=area)
            linea = Linea.objects.get(id=linea)
            a_f = ActivoFijo.objects.create(ubicacion = ubicacion, area = area, linea = linea, n_activo_sap = n_activo_sap, n_pedimento = n_pedimento, principal = principal, descripcion = descripcion, marca = marca, modelo = modelo, n_serie = n_serie, id_adicional = id_adicional, año = año, pais_origen = pais_origen)
            a_f.consecutivo = f"LC{a_f.id}"
            a_f.save()
            data = {"msg": "Creado activo fijo"}
            code = status.HTTP_201_CREATED
        except Exception as err:
            data = {"error": str(err)}
            code = status.HTTP_400_BAD_REQUEST
        return Response(data, status = code)
        

class ListLastFiveActivoFijo(APIView):
    
    def get(self, request):
        data = ActivoFijo.objects.all().order_by('-id')[:5].values()
        print(data)
        return Response(data)
        
        