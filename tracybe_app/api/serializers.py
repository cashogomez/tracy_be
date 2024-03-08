from rest_framework import serializers
from datetime import datetime, timezone
from tracybe_app.models import (Instrumento,  Set, Empaque, TipoEquipo, Turno, Etapa, AreaSolicitante, Evento,Equipo, 
                                EventoLavado, Ciclo)


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        exclude = ['empaque']
        #fields = '__all__'
    
class AreaSolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaSolicitante
        fields = '__all__'

class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

class EventoLavadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoLavado
        fields = '__all__'


class InstrumentoSerializer(serializers.ModelSerializer):
    longitud_codigo_qr = serializers.SerializerMethodField()
    listainstrumentoeventolavado = EventoLavadoSerializer(many=True, read_only = True)
    
    class Meta:
        model = Instrumento
        fields = '__all__'
        #fields = ['id', 'nombre', 'tipo']
        #exclude = ['id']
    
    def get_longitud_codigo_qr(self, object):
        if object.codigo_qr is None:
            caracteres = 0
        else:
            caracteres = len(object.codigo_qr)
        return caracteres
        
    def validate(self, data):
        if data['nombre']==data['tipo']:
            raise serializers.ValidationError('El nombre y el tipo deben ser diferentes')
        else:
            return data
        
    def validate_codigo_qr(self, data):
        if len(data) < 4:
            raise serializers.ValidationError('El código QR es muy corto')
        else:
            return data
        
        

class SetSerializer(serializers.ModelSerializer):
    #listainstrumento = InstrumentoSerializer(many=True, read_only = True)
    #listainstrumento = serializers.StringRelatedField(many=True)
    #listainstrumento = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    listainstrumento = serializers.HyperlinkedRelatedField (
        many=True, 
        read_only = True,
        view_name="instrumento-detail"
        )
    
    class Meta:
        model = Set
        fields = "__all__"

class EmpaqueSerializer(serializers.ModelSerializer):
    semaforo = serializers.SerializerMethodField()
    listaempaqueset = SetSerializer(many=True, read_only = True)
    listaempaqueinstrumento = InstrumentoSerializer(many = True, read_only = True)
    listaempaqueevento = EventoSerializer(many = True, read_only = True)
    
    
    class Meta:
        model = Empaque
        fields = "__all__"
        
    def get_semaforo(self, object):
        dias_caduca = object.caducidad
        ahora = datetime.now(timezone.utc)
        if object.created is not None:
            creado = object.created
            delta = creado - ahora
            if dias_caduca > 0:
                pc = delta.days // dias_caduca
                if pc < int(0.3*dias_caduca):
                    return 'B'
                elif pc>= int(0.3*dias_caduca) and pc < int(0.7*dias_caduca):
                    return 'I'
                elif pc>= int(0.7*dias_caduca) and pc <= dias_caduca:
                    return 'A'
                else:
                    return 'C'
            else:
                return 'E'
        else:
            return 'E'
        

class EquipoSerializer(serializers.ModelSerializer):
    listaequipoeventolavado = EventoLavadoSerializer(many = True, read_only = True)
    class Meta:
        model = Equipo
        fields = '__all__'
        

class CicloSerializer(serializers.ModelSerializer):
    equipos = EquipoSerializer(many=True, read_only=True)
    class Meta:
        model = Ciclo
        fields = '__all__'
        
class TipoEquipoSerializer(serializers.ModelSerializer):
    listatipoequipoequipo = EquipoSerializer(many=True, read_only=True)
    class Meta:
        model = TipoEquipo
        fields = '__all__'