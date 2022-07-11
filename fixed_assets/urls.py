from django.urls import path, include
from .views import Ping
from rest_framework.routers import DefaultRouter

urlpatterns = [   
path('ping/',Ping.as_view()),
# path("", include(router.urls)),
]