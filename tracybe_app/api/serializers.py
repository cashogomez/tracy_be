from rest_framework import serializers
from datetime import datetime, timezone
from tracybe_app.models import (CiclosEquipo, Instrumento,  InstrumentoSet, InstrumentoTicket, MaterialEmpaque,  Set, Empaque, SetEmpaque, SetTicket, Ticket, TipoEquipo, Turno, Etapa, AreaSolicitante, Evento,Equipo, 
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
        extra_kwargs = {'sets': {'required': False}, 'empaques': {'required': False}}
    
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
    #listainstrumento = serializers.StringRelatedField(many=True)
    #listainstrumento = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    #listainstrumento = serializers.HyperlinkedRelatedField (
    #    many=True, 
    #    read_only = True,
    #    view_name="instrumento-detail"
    #    )
    
    class Meta:
        model = Set
        fields = "__all__"
        extra_kwargs = {'empaques': {'required': False}}
#*******************************************************************
class MaterialEmpaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialEmpaque
        fields = "__all__"
        
        
#*******************************************************************

class EmpaqueSerializer(serializers.ModelSerializer):
    #semaforo = serializers.SerializerMethodField()
    #listaempaqueevento = EventoSerializer(many = True, read_only = True)
    materialempaque = MaterialEmpaqueSerializer()
    set = SetSerializer()
    
    class Meta:
        model = Empaque
        fields = "__all__"
        
    def create(self, validated_data) -> Empaque:
        empaque = Empaque.objects.create(**validated_data)
        return empaque
    
    def update(self, instance, validated_data) -> Empaque:
        instance.save()
        return instance
    
    
    # def get_semaforo(self, object):
    #     dias_caduca = object.caducidad
    #     ahora = datetime.now(timezone.utc)
    #     if object.created is not None:
    #         creado = object.created
    #         delta = creado - ahora
    #         if dias_caduca > 0:
    #             pc = delta.days // dias_caduca
    #             if pc < int(0.3*dias_caduca):
    #                 return 'B'
    #             elif pc>= int(0.3*dias_caduca) and pc < int(0.7*dias_caduca):
    #                 return 'I'
    #             elif pc>= int(0.7*dias_caduca) and pc <= dias_caduca:
    #                 return 'A'
    #             else:
    #                 return 'C'
    #         else:
    #             return 'E'
    #     else:
    #         return 'E'
        
# **************************** SERIALIZER Multy Multy ***************************
class InstrumentoSetSerializer(serializers.ModelSerializer):
    instrumento = InstrumentoSerializer()
    set = SetSerializer()

    class Meta:
        model = InstrumentoSet
        fields = "__all__"

    def create(self, validated_data) -> InstrumentoSet:

        # create connection
        conn = InstrumentoSet.objects.create(**validated_data)
        return conn

# class InstrumentoEmpaqueSerializer(serializers.ModelSerializer):
#     instrumento = InstrumentoSerializer()
#     empaque = EmpaqueSerializer()

#     class Meta:
#         model = InstrumentoEmpaque
#         fields = "__all__"

#     def create(self, validated_data) -> InstrumentoEmpaque:
        
#         # create connection
#         conn = InstrumentoEmpaque.objects.create(**validated_data)
#         return conn

class SetEmpaqueSerializer(serializers.ModelSerializer):
    set = SetSerializer()
    empaque = EmpaqueSerializer()

    class Meta:
        model = SetEmpaque
        fields = "__all__"

    def create(self, validated_data) -> SetEmpaque:

        # create connection
        conn = SetEmpaque.objects.create(**validated_data)
        return conn

#*******************************************************************
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

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {'sets': {'required': False}, 'instrumentos': {'required': False}}
        
# **************************** Multi Multi ticket serializer ****************************
class SetTicketSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()
    set = SetSerializer()

    class Meta:
        model = SetTicket
        fields = "__all__"

    def create(self, validated_data) -> SetTicket:
        # create connection
        conn = SetTicket.objects.create(**validated_data)
        return conn
    
    def update(self, instance, validated_data) -> SetTicket:
        #instance.ticket = validated_data.get('ticket', instance.ticket)
        #instance.set = validated_data.get('set', instance.set)
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        #print('--------------------------')
        #print(instance.ticket)
        #conn = SetTicket.objects.update(**validated_data)
        instance.save()
        return instance


class InstrumentoTicketSerializer(serializers.ModelSerializer):
    instrumento = InstrumentoSerializer()
    ticket = TicketSerializer()

    class Meta:
        model = InstrumentoTicket
        fields = "__all__"

    def create(self, validated_data) -> InstrumentoTicket:

        # create connection
        conn = InstrumentoTicket.objects.create(**validated_data)
        return conn
    
    def update(self, instance, validated_data) -> InstrumentoTicket:
        #instance.ticket = validated_data.get('ticket', instance.ticket)
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        print('--------------------------')
        print(instance)
        #conn = InstrumentoTicket.objects.update(**validated_data)
        instance.save()
        return instance

class CiclosEquipoSerializer(serializers.ModelSerializer):
    ciclo = CicloSerializer()
    Equipo = EquipoSerializer()

    class Meta:
        model = CiclosEquipo
        fields = "__all__"

    def create(self, validated_data) -> CiclosEquipo:
        # create connection
        conn = CiclosEquipo.objects.create(**validated_data)
        return conn
    
    def update(self, instance, validated_data) -> CiclosEquipo:
        #instance.ticket = validated_data.get('ticket', instance.ticket)
        #instance.set = validated_data.get('set', instance.set)
        #instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        #print('--------------------------')
        #print(instance.ticket)
        #conn = SetTicket.objects.update(**validated_data)
        instance.save()
        return instance

