from django.db import models

"""
Modelos creados a partir de la siguiente fuente:
https://docs.google.com/spreadsheets/d/1hAmNRQb8-N3EoptTpiAcyhO_X-Qns3CV/edit?usp=sharing&ouid=110855647692152758160&rtpof=true&sd=true


"""

# Create your models here.
class Ubicacion(models.Model):
    """
    Catalogo para manejar la ubicacion de los activos fijos
    Ejemplos: 
        Planta 1
        Planta 2
        Laboratorios
    """
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.name}"


class Area(models.Model):
    """
    Catalogo para manejar el área donde se encuentra en uso el activo fijo
    Ejemplos:
        Prensas
        Cigueñal
        Pre Ensamble
        null
    """
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.name}"


class Linea(models.Model):
    """
    Catalogo para manejar la linea donde se encuentra trabajando el activo fijo.
    Ejemplos:
        L1
        L2
        L3
        Calorimetros EM3
    """
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.name}"


class StatusActivo(models.Model):
    """
    Catalogo para manejar el estado del activo fijo
    Ejemplos:
        Verde
        Amarillo
        Rojo

    Referencia: https://docs.google.com/spreadsheets/d/1hAmNRQb8-N3EoptTpiAcyhO_X-Qns3CV/edit?pli=1#gid=1404005117
    """
    status = models.CharField(max_length=50)
    color = models.CharField(max_length=50) #color en hexadecimal

    def __str__(self) -> str:
        return f"{self.status} - {self.color}"

class ActivoFijo(models.Model):
    """
    Modelo para manejar el activo fijo con todos sus campos.
    """
    consecutivo = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True, blank=True)
    linea = models.ForeignKey(Linea, on_delete=models.DO_NOTHING, null=True, blank=True)
    # funcional = models.CharField(max_length=60, null=True, blank=True)
    n_activo_sap = models.CharField(max_length=100, null=True, blank=True)
    n_pedimento = models.CharField(max_length=100, null=True, blank=True)
    principal = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    marca = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=120, null=True, blank=True)
    n_serie = models.CharField(max_length=120, null=True, blank=True)
    id_adicional = models.CharField(max_length=120, null=True, blank=True) # identificador adicional
    año = models.DateField(null=True, blank=True)
    pais_origen = models.CharField(max_length=50, null=True, blank=True)
    is_consiliacion_completa = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.consecutivo} - {self.ubicacion} - {self.area} - {self.linea} - {self.n_activo_sap} - {self.n_pedimento} - {self.principal} - {self.descripcion} - {self.marca} - {self.modelo} - {self.n_serie} - {self.id_adicional} - {self.año} - {self.pais_origen} - {self.is_consiliacion_completa}"