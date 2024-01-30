from rest_framework.response import Response
from tracybe_app.api.permisos import IsAdminOrReadOnly, IsEventoUserOrReadOnly
from tracybe_app.models import Instrumento, Set, Empaque, TipoEquipo, Turno, Etapa, AreaSolicitante, Evento
from tracybe_app.models import Equipo, EventoLavado
from tracybe_app.api.serializers import InstrumentoSerializer, SetSerializer, EmpaqueSerializer, TipoEquipoSerializer, TurnoSerializer, EtapaSerializer, AreaSolicitanteSerializer, EventoSerializer
from tracybe_app.api.serializers import EquipoSerializer, EventoLavadoSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# *********************** TIPO de Equipo *******************
class CrearTipoEquipo(generics.CreateAPIView):
    queryset =  TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer
    
    
class ListaTipoEquipo(generics.ListCreateAPIView):
    queryset =  TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer

class DetalleTipoEquipo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer

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

#http://127.0.0.1:8000/instrumento/empaque/MjYtMTItMjAyMyAyMzowNTo0MA==
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
        serializer = EmpaqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
##### ******************      SET ********************************************

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

# ******************************* INSTRUMENTO ******************************

class InstrumentoAV(APIView):
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
            instrumento = Instrumento.objects.get(pk=pk)
        except Instrumento.DoesNotExist:
            return Response({'error': 'Instrumento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        instrumento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

