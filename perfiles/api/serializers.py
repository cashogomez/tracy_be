from rest_framework import serializers
from django.contrib.auth.models import User
from perfiles.models import AreaTrabajo, Perfil, Puesto

class PerfilSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = Perfil
        fields = ['username', 'email', 'password', 'password2', 'nombre', 'paterno', 'materno','telefono', 'foto']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'El password de confirmación no coincide'})
        if Perfil.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'El email del usuario ya existe'})
        
        #cuenta = User(email=self.validated_data['email'], username=self.validated_data['username'])
        perfil = Perfil.objects.create_user(
            nombre = self.validated_data['nombre'],
            paterno = self.validated_data['paterno'],
            materno = self.validated_data['materno'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            foto = self.validated_data['foto'],
            
            password = self.validated_data['password'],
        )
        perfil.telefono = self.validated_data['telefono']
        perfil.set_password(password)
        perfil.save()
        return perfil
    
class PuestoSerializer(serializers.ModelSerializer):
    listapuestoperfil = PerfilSerializer(many=True, read_only = True)
    class Meta:
        model = Puesto
        fields = '__all__'
        
class AreaTrabajoSerializer(serializers.ModelSerializer):
    listaareaperfil = PerfilSerializer(many=True, read_only = True)
    class Meta:
        model = AreaTrabajo
        fields = '__all__'

        
