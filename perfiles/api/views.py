from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from perfiles.api.serializers import AreaTrabajoSerializer, PerfilSerializer, PuestoSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
#from perfiles import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from rest_framework.permissions import IsAuthenticated

from perfiles.models import AreaTrabajo, Perfil, Puesto

from rest_framework.views import APIView

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
            data['foto'] = cuenta.foto
            data['puesto'] = cuenta.puesto
            data['area'] = cuenta.area
            data['empresa_id'] = cuenta.empresa_id
            data['numeroEmpleado'] = cuenta.numeroEmpleado
            data['is_admin'] = cuenta.is_admin
            data['is_staff'] = cuenta.is_staff
            data['is_active'] = cuenta.is_active
            data['is_superadmin'] = cuenta.is_superadmin
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
    print('*************************************')
    print(request.headers)
    print('********************************')
    print(request.data)
    print('++++++++++++++++++++++++++++++++')
    if request.method == 'POST':
        print(request.user)
        return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
def perfil_view(request):
    if request.method == 'POST':
        print('11111111111111111111111111111111111')
        print(request.data)
        print('11111111111111111111111111111111')
        serializer = PerfilSerializer(data=request.data)
        data = {}

        
        if serializer.is_valid():
            cuenta = serializer.save()
            print('********************************')
            print(cuenta.puesto)
            print('++++++++++++++++++++++++++++++++')
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = cuenta.username
            data['email'] = cuenta.email
            data['nombre'] = cuenta.nombre
            data['paterno'] = cuenta.paterno
            data['materno'] = cuenta.materno
            data['telefono'] = cuenta.telefono
            data['foto'] = cuenta.foto
            data['puesto'] = cuenta.puesto
            data['area'] = cuenta.area
            data['empresa_id'] = cuenta.empresa_id
            data['numeroEmpleado'] = cuenta.numeroEmpleado
            data['is_admin'] = cuenta.is_admin
            data['is_staff'] = cuenta.is_staff
            data['is_active'] = cuenta.is_active
            data['is_superadmin'] = cuenta.is_superadmin
            refresh = RefreshToken.for_user(cuenta)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            print('$$$$$$$$$$$$$$$$$$$$$')
            data = serializer.errors
            print(data)
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(data)
    
@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method=='POST':
        email = request.data.get('email')
        print(email)
        password = request.data.get('password')
        
        perfil = auth.authenticate(email=email, password=password)
        
        if perfil is not None:
            data['response'] = 'El login fue exitoso'
            data['username'] = perfil.username
            data['email'] = perfil.email
            data['nombre'] = perfil.nombre
            data['paterno'] = perfil.paterno
            data['materno'] = perfil.materno
            data['telefono'] = perfil.telefono
            data['foto'] = perfil.foto
            data['puesto'] = perfil.puesto
            data['area'] = perfil.area
            data['empresa_id'] = perfil.empresa_id
            data['numeroEmpleado'] = perfil.numeroEmpleado
            data['is_admin'] = perfil.is_admin
            data['is_staff'] = perfil.is_staff
            data['is_active'] = perfil.is_active
            data['is_superadmin'] = perfil.is_superadmin
            refresh = RefreshToken.for_user(perfil)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "credenciales incorrectas"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# ************************ ETAPA **********************
class PuestoAV(APIView):
    def get(self, request):
        puestos = Puesto.objects.all()
        serializer = PuestoSerializer(puestos, many=True, context = {"request": request})
        return Response(serializer.data)
    
# ************************ ETAPA **********************
class AreaTrabajoAV(APIView):
    def get(self, request):
        areatrabajos = AreaTrabajo.objects.all()
        serializer = AreaTrabajoSerializer(areatrabajos, many=True, context = {"request": request})
        return Response(serializer.data)
    