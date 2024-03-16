from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from perfiles.models import Perfil
import datetime 

# Create your models here.

#*************** area que realiza la solicitud de los tickets a la ceye ***************
# el tipo puede ser interna o externa
# el nombre puede ser quirofano, urgencia etc y la externa dese ser el nombre del proveedor


    
class AreaSolicitante(models.Model):
    tipo = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tipo+' '+self.nombre
    

class Turno(models.Model):
    numero = models.IntegerField(default=0)
    inicio = models.TimeField(default=datetime.time(8, 0, 0) ) 
    fin = models.TimeField(default=datetime.time(15, 0, 0))
    
    def __str__(self):
        return 'Turno '+str(self.numero)
    
class Etapa(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    
class  Empaque(models.Model):
    tipo = models.CharField(max_length=250)
    caracteristica = models.CharField(max_length=250,null=True, blank=True, default='')
    marca = models.CharField(max_length=250,null=True, blank=True, default='')
    modelo = models.CharField(max_length=250,null=True, blank=True, default='')
    codigo_qr = models.CharField(max_length=250, null=True, blank=True, default='')
    caducidad = models.PositiveSmallIntegerField()
    #  rojo = 30 % de los ultimos dias
    #  naranja = 40% de los siguientes dias
    #  amarillo = 30% de los primeros dias
    # la semaforizacion es para cada empaque
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.tipo +' '+self.caracteristica

class Set(models.Model):
    numero = models.PositiveIntegerField(null=True, default=0)
    maximo = models.PositiveIntegerField(null=True, default=0)
    minimo = models.PositiveIntegerField(null=True, default=0)
    nombre = models.CharField(max_length=250)
    foto = models.URLField(max_length=250, null=True, blank=True, default='')
    activo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

    
class Evento(models.Model):
    empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE,  null=True, related_name="listaempaqueevento")
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaperfilevento")
    entrego = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaentregoevento")
    recepciono = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listarecepcionoevento")
    devolvio = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listadevolvioevento")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank=True, null=True, related_name="listaetapaevento")
    folioPBD = models.CharField(max_length=250, null=True, blank=True, default='')
    folioPB = models.CharField(max_length=250, null=True, blank=True, default='')
    folioPQ = models.CharField(max_length=250, null=True, blank=True, default='')
    descripcion = models.CharField(max_length=250, null=True, blank=True, default='')
    incidencia = models.CharField(max_length=250, null=True, blank=True, default='')
    notas = models.CharField(max_length=900, null=True, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Evento: ' + self.descripcion
    
class Estatus(models.Model):
    nombre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre

class TipoEquipo(models.Model):
    nombre = models.CharField(max_length= 250)
    def __str__(self):
        return self.nombre
    
    
class Ciclo(models.Model):
    nombre = models.CharField(max_length=250)
    duracion = models.TimeField(default=datetime.time(8, 0, 0) ) 
    temperatura = models.IntegerField(default=120, null=True, blank=True)
    
    
    def __str__(self):
        return 'Ciclo ' + self.nombre
    
class Equipo(models.Model):
    numero = models.PositiveSmallIntegerField()
    tipoequipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE, related_name="listatipoequipoequipo")
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, related_name="listaestatusequipo")
    ciclos = models.ManyToManyField(Ciclo, related_name='equipos', blank=True)
    marca = models.CharField(max_length=250, blank=True, null = True, default='')
    modelo = models.CharField(max_length=250, blank=True, null = True, default='')
    numero_serie = models.CharField(max_length=250, blank=True, null = True, default='')
    
    def __str__(self):
        return self.tipoequipo.nombre+' '+str(self.numero)

    
class Instrumento(models.Model):
    nombre = models.CharField(max_length=250)
    cantidad  = models.IntegerField( null=True, blank=True, default=0)
    familia = models.CharField(max_length=250, null=True, blank=True, default='')
    individuo = models.IntegerField( null=True, blank=True, default=0)
    tipo = models.CharField(max_length=250, null=True, blank=True, default='')
    marca = models.CharField(max_length=250, null=True, blank=True, default='')
    lote =  models.CharField(max_length=250, null=True, blank=True, default='')
    foto = models.URLField(max_length=250, null=True, blank=True, default='')
    descripcion = models.CharField(max_length=500, null=True, blank=True, default='')
    uso = models.IntegerField( null=True, blank=True, default=0)
    codigo_qr = models.CharField(max_length=250, null=True, blank=True, default='')
    prelavado = models.BooleanField(default=False)
    completo = models.BooleanField(default=True)
    funcional = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.nombre + ' ' + self.tipo+' '+self.marca + ' ' + self.descripcion

class cantidadInstrumentos(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE, blank=True, null=True, related_name="listasetcantidadinstrumento")
    empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE, blank=True, null=True, related_name="listaempaquecantidadinstrumento")
    instrumento = models.OneToOneField(
        Instrumento,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cantidad = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return 'son '+self.cantidad + ' '+self.instrumento.nombre

class cantidadSet(models.Model):
    empaque = models.ForeignKey(Empaque, on_delete=models.CASCADE, blank=True, null=True, related_name="listaempaquecantidadset")
    set = models.OneToOneField(
        Set,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cantidad = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return 'son '+self.cantidad + ' '+self.set.nombre

class EventoLavado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaperfileventolavado")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True, related_name="listaequipoeventolavado")
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, blank=True, null=True, related_name="listainstrumentoeventolavado")
    duracion = models.TimeField(default=datetime.time(8, 0, 0) ) 
    inicio = models.BooleanField(default=False)
    paro = models.BooleanField(default=False)
    finalizado= models.BooleanField(default=False)
    incidencia = models.CharField(max_length=250, null=True, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Evento Lavado: ' + str(self.created)

    
class Paciente(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True, default='')
    paterno = models.CharField(max_length=250, null=True, blank=True, default='')
    materno = models.CharField(max_length=250, null=True, blank=True, default='')
    fecha_nacimiento = models.DateTimeField(null=True, blank=True,default='2021-12-31 15:25:00+01')
    numero_habitacion =  models.CharField(max_length=250, null=True, blank=True, default='')
    diagnostico = models.CharField(max_length=250, null=True, blank=True, default='')
    
    def __str__(self):
        return  self.nombre+self.paterno+self.materno
    
class Ticket(models.Model):
    fecha_cirugia = models.DateTimeField(default='2021-12-31 15:25:00+01')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True, related_name="listapacienteticket")
    sala = models.CharField(max_length=100, null=True, blank=True, default='')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, blank=True, null=True, related_name="listaturnoticket")
    cirugia = models.CharField(max_length=250, null=True, blank=True, default='')
    solicita = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listasolicitaticket")
    cirujano = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listacirujanoticket")
    anestesiologo = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaanestesiologoticket")
    residente = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaresidenteticket")
    area_registro = models.ForeignKey(AreaSolicitante, on_delete=models.CASCADE, blank=True, null=True, related_name="listaarearegistroticket")
    enfermero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name="listaenfermeroticket")
    # prioridad 1 es alta, prioridad 2 es media, prioridad 3 es baja
    prioridad = models.PositiveSmallIntegerField()
    set = models.ForeignKey(Set, on_delete=models.CASCADE, blank=True, null=True, related_name="listasetticket")
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, blank=True, null=True, related_name="listainstrumentoticket")
    notas = models.CharField(max_length=900, null=True, blank=True, default='')
    activo = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return  'Ticket '+str(self.id)
    