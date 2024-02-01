
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Puesto(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo
    
class AreaTrabajo(models.Model):
    tipo = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tipo+' '+self.nombre
   

class MiPerfilManager(BaseUserManager):
    def create_user(self, nombre, paterno, materno, username, email, foto,  puesto, area, empresa_id, numeroEmpleado, is_active, is_staff, is_admin, is_superadmin,  password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        
        if not username:
            raise ValueError('El usuario debe tener un username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            nombre = nombre,
            paterno = paterno,
            materno = materno,
            foto = foto,
            puesto = puesto,
            area = area,
            empresa_id = empresa_id,
            numeroEmpleado = numeroEmpleado,
            is_admin = is_admin,
            is_active = is_active,
            is_staff = is_staff,
            is_superadmin = is_superadmin
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nombre, paterno, materno, username, email, foto, puesto, area, empresa_id, numeroEmpleado,  password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            nombre = nombre,
            paterno = paterno,
            materno = materno,
            foto = foto,
            puesto = puesto,
            area = area,
            empresa_id = empresa_id,
            numeroEmpleado = numeroEmpleado
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
        

class Perfil(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50)
    foto = models.CharField(max_length=500, null=True, blank=True, default='')
    
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, blank=True, null=True, related_name="listapuestoperfil")
    area =  models.ForeignKey(AreaTrabajo, on_delete=models.CASCADE, blank=True, null=True, related_name="listaareaperfil")
    empresa_id =  models.CharField(max_length=50)
    numeroEmpleado = models.CharField(max_length=50)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'paterno', 'materno']
    
    objects = MiPerfilManager()
    
    def nombre_completo(self):
        return f'{self.nombre} {self.paterno} {self.materno}'
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True