from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [   
    path('ping/', Ping.as_view()),
    path('list-ubicacion', ListUbicacion.as_view()),
    path('list-area', ListArea.as_view()),
    path('list-linea', ListLinea.as_view()),
    path('list-status-activo', ListStatusActivo.as_view()),
    path('list-last-five', ListLastFiveActivoFijo.as_view()),
    path('detail-a-f', ListDetailActivoFijo.as_view()), # a- f: activo fijo
    path('create-activo-fijo', CreateActivoFijo.as_view()),
]