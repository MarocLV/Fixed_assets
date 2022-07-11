from django.contrib import admin
from .models import *

admin.site.register(Ubicacion)
admin.site.register(Area)
admin.site.register(Linea)
admin.site.register(StatusActivo)
admin.site.register(ActivoFijo)

