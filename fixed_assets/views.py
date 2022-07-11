from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from authentication.authTokentodoapp import CsrfExemptSessionAuthentication, BasicAuthentication

# Create your views here.
class Ping(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request):
        return Response({'msg': 'Pong. API live'},status=status.HTTP_200_OK)