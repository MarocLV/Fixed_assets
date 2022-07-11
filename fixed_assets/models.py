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
    pass

class Area(models.Model):
    """
    Catalogo para manejar el área donde se encuentra en uso el activo fijo
    Ejemplos:
        Prensas
        Cigueñal
        Pre Ensamble
        null
    """
    pass

class Linea(models.Model):
    """
    Catalogo para manejar la linea donde se encuentra trabajando el activo fijo.
    Ejemplos:
        L1
        L2
        L3
        Calorimetros EM3
    """
    pass

class StatusActivo(models.Model):
    """
    Catalogo para manejar el estado del activo fijo
    Ejemplos:
        Verde
        Amarillo
        Rojo

    Referencia: https://docs.google.com/spreadsheets/d/1hAmNRQb8-N3EoptTpiAcyhO_X-Qns3CV/edit?pli=1#gid=1404005117
    """
    pass

class ActivoFijo(models.Model):
    """
    Modelo para manejar el activo fijo con todos sus campos.
    """
    pass