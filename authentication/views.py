import email
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate, login

from .authTokentodoapp import CsrfExemptSessionAuthentication, BasicAuthentication

# Create your views here.

class UserView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    #Esta función corrige el error por csrf, se puede omitir cuando en el formulario se agrega csrf token
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """ Register a new user"""
        
        if request.method == 'POST':
            jd = json.loads(request.body)
            User.objects.create(username=jd['username'], first_name=jd['first_name'],last_name=jd['last_name'],email=jd['email'],
            password=make_password(jd['password']))
            datos={'msg':'registered user'}
            return Response(datos, status=status.HTTP_201_CREATED) 
        else:
            datos={'msg':'user not registered'}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)  
        

class Login(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        email = request.data.get('email', None)            
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response({'error': 'wrong user or password'},status=status.HTTP_400_BAD_REQUEST)

class CustomUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()