from rest_framework import serializers
from .models import *

class UbicacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ubicacion
        fields = '__all__'
        
        
class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = '__all__'
        
        
class LineaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Linea
        fields = '__all__'


class StatusActivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StatusActivo
        fields = '__all__'
        
        
class ActivoFijoSerializer(serializers.ModelSerializer):
    
    ubicacion = serializers.SerializerMethodField('get_ubicacion')
    area = serializers.SerializerMethodField('get_area')
    linea = serializers.SerializerMethodField('get_linea')
    
    class Meta:
        model = ActivoFijo
        fields = '__all__'

    def get_ubicacion(self, ActivoFijo):
        try:
            data = {"nombre": ActivoFijo.ubicacion.name}
        except:
            data = None
        return data    
    
    def get_area(self, ActivoFijo):
        try:
            data = {"nombre": ActivoFijo.area.name}
        except:
            data = None
        return data    
    
    def get_linea(self, ActivoFijo):
        try:
            data = {"nombre": ActivoFijo.linea.name}
        except:
            data = None
        return data    