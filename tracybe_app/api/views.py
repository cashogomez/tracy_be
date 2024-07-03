from rest_framework.response import Response
from tracybe_app.api.permisos import IsAdminOrReadOnly, IsEventoUserOrReadOnly
from tracybe_app.models import Ciclo, CiclosEquipo, Estatus, EventoEsterilizacion, Instrumento, InstrumentoSet, InstrumentoTicket, MaterialEmpaque, MaterialEnEsterilizador, ReporteIncidencia, Set, Empaque, SetEmpaque, SetTicket, SetTicketOA, Ticket, TicketOA, Turno, Etapa, AreaSolicitante, Evento
from tracybe_app.models import Equipo, EventoLavado
from tracybe_app.api.serializers import  CicloSerializer, CiclosEquipoSerializer, EstatusSerializer, EventoEsterilizacionSerializer, InstrumentoSerializer, InstrumentoSetSerializer, InstrumentoTicketSerializer, MaterialEmpaqueSerializer, MaterialEnEsterilizadorSerializer, ReporteIncidenciaSerializer, SetEmpaqueSerializer, SetSerializer, EmpaqueSerializer, SetTicketOASerializer, SetTicketSerializer, TicketOASerializer, TicketSerializer, TurnoSerializer, EtapaSerializer, AreaSolicitanteSerializer, EventoSerializer
from tracybe_app.api.serializers import EquipoSerializer, EventoLavadoSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



# ************************ Evento ***************************
class EventoCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventoSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        empaque = Empaque.objects.get(pk=pk)
        serializer.save(empaque=empaque)
        
class ListaEvento(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventoSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Evento.objects.filter(empaque=pk)
        
    
class DetalleEvento(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


# ************************ Área Solicitante  **********************
class AreaSolicitanteAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        areassolicitantes = AreaSolicitante.objects.all()
        serializer = AreaSolicitanteSerializer(areassolicitantes, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AreaSolicitanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleAreaSolicitanteAV(APIView):
    def get(self, request, pk):
        try:
            areasolicitante = AreaSolicitante.objects.get(pk=pk)
        except AreaSolicitante.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AreaSolicitanteSerializer(areasolicitante, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            areasolicitante = AreaSolicitante.objects.get(pk=pk)
        except AreaSolicitante.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AreaSolicitanteSerializer(areasolicitante, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            areasolicitante = AreaSolicitante.objects.get(pk=pk)
        except AreaSolicitante.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        areasolicitante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# ************************ ETAPA **********************
class EtapaAV(APIView):
    def get(self, request):
        etapas = Etapa.objects.all()
        serializer = EtapaSerializer(etapas, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EtapaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleEtapaAV(APIView):
    def get(self, request, pk):
        try:
            etapa = Etapa.objects.get(pk=pk)
        except Etapa.DoesNotExist:
            return Response({'error': 'La etapa no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EtapaSerializer(etapa, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            etapa = Etapa.objects.get(pk=pk)
        except Etapa.DoesNotExist:
            return Response({'error': 'La etapa no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EtapaSerializer(etapa, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            etapa = Etapa.objects.get(pk=pk)
        except Etapa.DoesNotExist:
            return Response({'error': 'La etapa no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        etapa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# ************************  TURNO **********************
class TurnoAV(APIView):
    def get(self, request):
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleTurnoAV(APIView):
    def get(self, request, pk):
        try:
            turno = Turno.objects.get(pk=pk)
        except Turno.DoesNotExist:
            return Response({'error': 'Turno no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TurnoSerializer(turno, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            turno = Turno.objects.get(pk=pk)
        except Turno.DoesNotExist:
            return Response({'error': 'Turno no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TurnoSerializer(turno, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            turno = Turno.objects.get(pk=pk)
        except Turno.DoesNotExist:
            return Response({'error': 'Turno no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        turno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

##### ************************ EMPAQUE *************************

class BusquedaEmpaqueAV(APIView):
    def get(self, request, cadena):
        empaques = Empaque.objects.filter(codigo_qr__contains=cadena)
        serializer = EmpaqueSerializer(empaques, many=True)
    
        data = {
            "Keyword": cadena,
            "results": serializer.data
        }
        return Response(data)
class EmpaqueAV(APIView):
    def get(self, request):
        empaques = Empaque.objects.all()
        serializer = EmpaqueSerializer(empaques, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        #request.data['materialempaque'] = MaterialEmpaqueSerializer(request.data['materialempaque'])
        
        serializer = EmpaqueSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmpaqueCreate(generics.CreateAPIView):
    serializer_class = EmpaqueSerializer
    print ('Despues del serializer')
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        materialempaquereal = MaterialEmpaque.objects.get(pk=pk)
        serializer.save(materialempaque=materialempaquereal)
        
class DetalleEmpaqueAV(APIView):
    def get(self, request, pk):
        try:
            empaque = Empaque.objects.get(pk=pk)
        except Empaque.DoesNotExist:
            return Response({'error': 'Empaque no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpaqueSerializer(empaque, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            empaque = Empaque.objects.get(pk=pk)
        except Empaque.DoesNotExist:
            return Response({'error': 'Empaque no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpaqueSerializer(empaque, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            empaque = Empaque.objects.get(pk=pk)
        except Empaque.DoesNotExist:
            return Response({'error': 'Empaque no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        empaque.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
##### ***********************    SET  ********************************************

class SetAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        sets = Set.objects.all()
        serializer = SetSerializer(sets, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleSetAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            set = Set.objects.get(pk=pk)
        except Set.DoesNotExist:
            return Response({'error': 'Set no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SetSerializer(set, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            set = Set.objects.get(pk=pk)
        except Set.DoesNotExist:
            return Response({'error': 'Set no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SetSerializer(set, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            set = Set.objects.get(pk=pk)
        except Set.DoesNotExist:
            return Response({'error': 'Set no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
         
# ***************************** SET-EMPAQUE *********************************
class SetEmpaqueViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = SetEmpaque.objects.all()
    serializer_class = SetEmpaqueSerializer

class SetEmpaqueCreate(generics.CreateAPIView):
    serializer_class = SetEmpaqueSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        setreal = Set.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        empaquereal = Empaque.objects.get(pk=ik)
        serializer.save(set=setreal, empaque=empaquereal)
        
class ListaSetEmpaque(generics.ListCreateAPIView):
    serializer_class = SetEmpaqueSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return SetEmpaque.objects.filter(set=pk)
        
    
class DetalleSetEmpaque(generics.RetrieveUpdateDestroyAPIView):
    queryset = SetEmpaque.objects.all()
    serializer_class = SetEmpaqueSerializer


# ******************************* INSTRUMENTO ******************************

class InstrumentoAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        instrumentos = Instrumento.objects.all()
        serializer = InstrumentoSerializer(instrumentos, many = True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = InstrumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetalleInstrumentoAV(APIView):
    
    def get(self, request, pk):
        try:
            instrumento = Instrumento.objects.get(pk=pk) 
        except Instrumento.DoesNotExist:
            return Response({'error': 'Instrumento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InstrumentoSerializer(instrumento)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            instrumento = Instrumento.objects.get(pk=pk) 
        except Instrumento.DoesNotExist:
            return Response({'error': 'Instrumento no encontrado'}, status=status.HTTP_404_NOT_FOUND)     

        serializer = InstrumentoSerializer(instrumento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            print(pk)
            
            instrumento = Instrumento.objects.get(pk=pk)
            print(instrumento)
        except Instrumento.DoesNotExist:
            return Response({'error': 'Instrumento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        instrumento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ***********************  INSTRUMENTO-SET *************************

class InstrumentoSetViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = InstrumentoSet.objects.all()
    serializer_class = InstrumentoSetSerializer

class InstrumentoSetCreate(generics.CreateAPIView):
    print('Iniciando')
    serializer_class = InstrumentoSetSerializer
    print ('Despues del serializer')
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        setreal = Set.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        instrumentoreal = Instrumento.objects.get(pk=ik)
        serializer.save(set=setreal, instrumento=instrumentoreal)
        
class ListaInstrumentoSet(generics.ListCreateAPIView):
    serializer_class = InstrumentoSetSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return InstrumentoSet.objects.filter(set=pk)
        
    
class DetalleInstrumentoSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstrumentoSet.objects.all()
    serializer_class = InstrumentoSetSerializer
    
    def perform_update(self, serializer):
            try:
                instrumentoset = InstrumentoSet.objects.get(pk=self.kwargs['pk'])
            except InstrumentoSet.DoesNotExist:
                return Response({'error': 'Instrumento Set no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            if serializer.is_valid():
                serializer.save(set=instrumentoset.set, instrumento=instrumentoset.instrumento)
                return Response(serializer.data)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ***********************  CICLO - EQUIPO *************************

class CiclosEquipoViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = CiclosEquipo.objects.all()
    serializer_class = CiclosEquipoSerializer

class CiclosEquipoCreate(generics.CreateAPIView):
    print('Iniciando')
    serializer_class = CiclosEquipoSerializer
    print ('Despues del serializer')
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        equiporeal = Equipo.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        cicloreal = Ciclo.objects.get(pk=ik)
        serializer.save(ciclo=cicloreal, equipo=equiporeal)
        
class ListaCiclosEquipo(generics.ListCreateAPIView):
    serializer_class = CiclosEquipoSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return CiclosEquipo.objects.filter(equipo=pk)
        
    
class DetalleCiclosEquipo(generics.RetrieveUpdateDestroyAPIView):
    queryset = CiclosEquipo.objects.all()
    serializer_class = CiclosEquipoSerializer


# ********************** INSTRUMENTO-EMPAQUE ************************

# class InstrumentoEmpaqueViewSet(viewsets.ModelViewSet):
#     permission_classes = ()
#     queryset = InstrumentoEmpaque.objects.all()
#     serializer_class = InstrumentoEmpaqueSerializer   
# ******************************* Lavadora ******************************

class EquipoAV(APIView):
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetalleEquipoAV(APIView):
    
    def get(self, request, pk):
        try:
            equipo = Equipo.objects.get(pk=pk) 
        except Equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            equipo = Equipo.objects.get(pk=pk) 
        except Equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)     

        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            equipo = Equipo.objects.get(pk=pk)
        except Equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ******************************* EventoLavado ******************************

class EventoLavadoCreate(generics.CreateAPIView):
    serializer_class = EventoLavadoSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        equipo = Equipo.objects.get(pk=pk)
        serializer.save(equipo=equipo)
        
class ListaEventoLavado(generics.ListCreateAPIView):
    serializer_class = EventoLavadoSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return EventoLavado.objects.filter(lavadora=pk)
        
    
class DetalleEventoLavado(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventoLavado.objects.all()
    serializer_class = EventoLavadoSerializer

# *************************** TICKET **************************
class TicketAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many = True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetalleTicketAV(APIView):
    
    def get(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk) 
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk) 
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket no encontrado'}, status=status.HTTP_404_NOT_FOUND)     

        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            print('Ticket a borrar '+str(pk))
            
            ticket = Ticket.objects.get(pk=pk)
            print(ticket)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ***********************  INSTRUMENTO-Ticket *************************

class InstrumentoTicketViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = InstrumentoTicket.objects.all()
    serializer_class = InstrumentoTicketSerializer

class InstrumentoTicketCreate(generics.CreateAPIView):
    print('Iniciando')
    serializer_class = InstrumentoTicketSerializer
    print ('Despues del serializer')
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        ticketreal = Ticket.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        instrumentoreal = Instrumento.objects.get(pk=ik)
        serializer.save(ticket=ticketreal, instrumento=instrumentoreal)
        
class ListaInstrumentoTicket(generics.ListCreateAPIView):
    serializer_class = InstrumentoTicketSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return InstrumentoTicket.objects.filter(ticket=pk)
        
    
class DetalleInstrumentoTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstrumentoTicket.objects.all()
    serializer_class = InstrumentoTicketSerializer

# ***********************  Set-Ticket *************************

class SetTicketViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = SetTicket.objects.all()
    serializer_class = SetTicketSerializer

class SetTicketCreate(generics.CreateAPIView):
    print('Iniciando')
    serializer_class = SetTicketSerializer
    print ('Despues del serializer')
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        ticketreal = Ticket.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        setreal = Set.objects.get(pk=ik)
        serializer.save(ticket=ticketreal, set=setreal)
        
class ListaSetTicket(generics.ListCreateAPIView):
    serializer_class = SetTicketSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return SetTicket.objects.filter(ticket=pk)
        
    
class DetalleSetTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = SetTicket.objects.all()
    serializer_class = SetTicketSerializer
    
# ************************ Material Empaque  **********************
class MaterialEmpaqueAV(APIView):
    def get(self, request):
        areassolicitantes = MaterialEmpaque.objects.all()
        serializer = MaterialEmpaqueSerializer(areassolicitantes, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MaterialEmpaqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleMaterialEmpaqueAV(APIView):
    def get(self, request, pk):
        try:
            areasolicitante = MaterialEmpaque.objects.get(pk=pk)
        except MaterialEmpaque.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaterialEmpaqueSerializer(areasolicitante, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            areasolicitante = MaterialEmpaque.objects.get(pk=pk)
        except MaterialEmpaque.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaterialEmpaqueSerializer(areasolicitante, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            areasolicitante = MaterialEmpaque.objects.get(pk=pk)
        except MaterialEmpaque.DoesNotExist:
            return Response({'error': 'El área solicitante no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        areasolicitante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# ************************ Material Empaque  **********************
class CicloAV(APIView):
    def get(self, request):
        ciclossolicitantes = Ciclo.objects.all()
        serializer = CicloSerializer(ciclossolicitantes, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CicloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class DetalleCicloAV(APIView):
    def get(self, request, pk):
        try:
            ciclosolicitante = Ciclo.objects.get(pk=pk)
        except Ciclo.DoesNotExist:
            return Response({'error': 'El ciclo no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CicloSerializer(ciclosolicitante, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            ciclosolicitante = Ciclo.objects.get(pk=pk)
        except Ciclo.DoesNotExist:
            return Response({'error': 'El ciclo no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CicloSerializer(ciclosolicitante, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            ciclosolicitante = Ciclo.objects.get(pk=pk)
        except Ciclo.DoesNotExist:
            return Response({'error': 'El ciclo no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        ciclosolicitante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# ************************  ESTATUS **********************

class EstatusAV(APIView):
    def get(self, request):
        estatus = Estatus.objects.all()
        serializer = EstatusSerializer(estatus, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EstatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleEstatusAV(APIView):
    def get(self, request, pk):
        try:
            estatus = Estatus.objects.get(pk=pk)
        except Estatus.DoesNotExist:
            return Response({'error': 'Estatus no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TurnoSerializer(estatus, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            estatus = Estatus.objects.get(pk=pk)
        except Estatus.DoesNotExist:
            return Response({'error': 'Estatus no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EstatusSerializer(estatus, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            estatus = Estatus.objects.get(pk=pk)
        except Estatus.DoesNotExist:
            return Response({'error': 'Estatus no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        estatus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


# ************************ EventoEsterilizacion  **********************
class EventoEsterilizacionAV(APIView):
    def get(self, request):
        materialenesterilizador = EventoEsterilizacion.objects.all()
        serializer = EventoEsterilizacionSerializer(materialenesterilizador, many=True, context = {"request": request})
        return Response(serializer.data)
       

class DetalleEventoEsterilizacionAV(APIView):
    def get(self, request, pk):
        try:
            print(pk)
            eventoesterilizacion = EventoEsterilizacion.objects.get(pk=pk)
        except EventoEsterilizacion.DoesNotExist:
            return Response({'error': 'El evento de esterilizacion no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoEsterilizacionSerializer(eventoesterilizacion, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            materialenesterilizador = EventoEsterilizacion.objects.get(pk=pk)
        except EventoEsterilizacion.DoesNotExist:
            return Response({'error': 'El evento de esterilización no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoEsterilizacionSerializer(materialenesterilizador, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            eventoesterilizacion = EventoEsterilizacion.objects.get(pk=pk)
        except EventoEsterilizacion.DoesNotExist:
            return Response({'error': 'El evento de esterilizacion no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        eventoesterilizacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class EventoEsterilizacionCrearAV(generics.CreateAPIView):

    serializer_class = EventoEsterilizacionSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        print(pk)
        ciclo = Ciclo.objects.get(pk=pk)
        return(serializer.save(ciclo=ciclo))

class DetalleEventoEsterilizacionEsterilizadorAV(APIView):
    def get(self, request, pk):
        try:
            print(pk)
            eventoesterilizacion = EventoEsterilizacion.objects.filter(id_esterilizador=pk)
        except EventoEsterilizacion.DoesNotExist:
            return Response({'error': 'El evento de esterilizacion no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventoEsterilizacionSerializer(eventoesterilizacion, many=True, context={'request': request})
        return Response(serializer.data)  
    
    # ************************ MaterialEnEsterilizador  **********************
class MaterialEnEsterilizadorAV(APIView):
    def get(self, request):
        materialenesterilizador = MaterialEnEsterilizador.objects.all()
        serializer = MaterialEnEsterilizadorSerializer(materialenesterilizador, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MaterialEnEsterilizadorSerializer(data=request.data)
        print('Aqui voy')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class DetalleMaterialEnEsterilizadorAV(APIView):
    def get(self, request, pk):
        try:
            materialenesterilizador = MaterialEnEsterilizador.objects.get(pk=pk)
        except MaterialEnEsterilizador.DoesNotExist:
            return Response({'error': 'El Material en Esterilizador no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaterialEnEsterilizadorSerializer(materialenesterilizador, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            materialenesterilizador = MaterialEnEsterilizador.objects.get(pk=pk)
        except MaterialEnEsterilizador.DoesNotExist:
            return Response({'error': 'El ciclo no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaterialEnEsterilizadorSerializer(materialenesterilizador, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            materialenesterilizador = MaterialEnEsterilizador.objects.get(pk=pk)
        except MaterialEnEsterilizador.DoesNotExist:
            return Response({'error': 'El Material En Esterilizador no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        materialenesterilizador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class MaterialEnEsterilizadorCrearAV(generics.CreateAPIView):
    serializer_class = MaterialEnEsterilizadorSerializer

    def perform_create(self, serializer):
        return(serializer.save())
    
class DetalleMaterialEnEsterilizadorEsterilizadorAV(APIView):
    def get(self, request, pk):
        try:
            print(pk)
            materialesterilizador = MaterialEnEsterilizador.objects.filter(id_esterilizador=pk)
        except MaterialEnEsterilizador.DoesNotExist:
            return Response({'error': 'El material del esterilizador no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaterialEnEsterilizadorSerializer(materialesterilizador, many=True, context={'request': request})
        return Response(serializer.data)  

# ************************ TicketOA **********************
class TicketOAAV(APIView):
    def get(self, request):
        etapas = TicketOA.objects.all()
        serializer = TicketOASerializer(etapas, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TicketOASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleTicketOAAV(APIView):
    def get(self, request, pk):
        try:
            etapa = TicketOA.objects.get(pk=pk)
        except TicketOA.DoesNotExist:
            return Response({'error': 'El ticket de otras areas no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TicketOASerializer(etapa, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            etapa = TicketOA.objects.get(pk=pk)
        except TicketOA.DoesNotExist:
            return Response({'error': 'El ticket de otras areas  no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TicketOASerializer(etapa, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            etapa = TicketOA.objects.get(pk=pk)
        except TicketOA.DoesNotExist:
            return Response({'error': 'El ticket de otras areas no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        etapa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
    
# ***********************  Set-TicketOA *************************

class SetTicketOAViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = SetTicketOA.objects.all()
    serializer_class = SetTicketOASerializer

class SetTicketOACreate(generics.CreateAPIView):

    serializer_class = SetTicketOASerializer

    def perform_create(self, serializer):
        print('Iniciando')
        pk = self.kwargs.get('pk')
        ticketreal = TicketOA.objects.get(pk=pk)
        ik = self.kwargs.get('ik')
        setreal = Set.objects.get(pk=ik)
        serializer.save(ticket=ticketreal, set=setreal)
        
class ListaSetTicketOA(generics.ListCreateAPIView):
    serializer_class = SetTicketOASerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return SetTicketOA.objects.filter(ticket=pk)
        
    
class DetalleSetTicketOA(generics.RetrieveUpdateDestroyAPIView):
    queryset = SetTicketOA.objects.all()
    serializer_class = SetTicketOASerializer
    
    
  
  
# ************************ ReporteIncidencia **********************
class ReporteIncidenciaAV(APIView):
    def get(self, request):
        etapas = ReporteIncidencia.objects.all()
        serializer = ReporteIncidenciaSerializer(etapas, many=True, context = {"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReporteIncidenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleReporteIncidenciaAV(APIView):
    def get(self, request, pk):
        try:
            etapa = ReporteIncidencia.objects.get(pk=pk)
        except ReporteIncidencia.DoesNotExist:
            return Response({'error': 'Reporte No Encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReporteIncidenciaSerializer(etapa, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            etapa = ReporteIncidencia.objects.get(pk=pk)
        except ReporteIncidencia.DoesNotExist:
            return Response({'error': 'Reporte No Encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReporteIncidenciaSerializer(etapa, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            etapa = ReporteIncidencia.objects.get(pk=pk)
        except ReporteIncidencia.DoesNotExist:
            return Response({'error': 'El ticket de otras areas no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)
        etapa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
  