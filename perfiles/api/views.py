from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from perfiles.api.serializers import PerfilSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
#from perfiles import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from rest_framework.permissions import IsAuthenticated

from tracy_be.perfiles.models import Perfil

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def session_view(request):
    if request.method == 'GET':
        user = request.user
        cuenta = Perfil.objects.get(email=user)
        data = {}
        if cuenta is not None:
            data['response'] = 'El usuario esta en sesión'
            data['username'] = cuenta.username
            data['email'] = cuenta.email
            data['nombre'] = cuenta.nombre
            data['paterno'] = cuenta.paterno
            data['materno'] = cuenta.materno
            data['telefono'] = cuenta.telefono
            refresh = RefreshToken.for_user(cuenta)
            data['token'] = {
                'refresh' : str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = 'El usuario no existe'
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
def perfil_view(request):
    if request.method == 'POST':
        serializer = PerfilSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            cuenta = serializer.save()
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = cuenta.username
            data['email'] = cuenta.email
            data['nombre'] = cuenta.nombre
            data['paterno'] = cuenta.paterno
            data['materno'] = cuenta.materno
            data['telefono'] = cuenta.telefono
            #token = Token.objects.get(user=cuenta).key
            #data['token']= token
            refresh = RefreshToken.for_user(cuenta)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors
            
        return Response(data)
    
@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method=='POST':
        email = request.data.get('email')
        password = request.data.get('password')
        
        perfil = auth.authenticate(email=email, password=password)
        
        if perfil is not None:
            data['response'] = 'El login fue exitoso'
            data['username'] = perfil.username
            data['email'] = perfil.email
            data['paterno'] = perfil.paterno
            data['materno'] = perfil.materno
            data['telefono'] = perfil.telefono
            refresh = RefreshToken.for_user(perfil)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "credenciales incorrectas"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    