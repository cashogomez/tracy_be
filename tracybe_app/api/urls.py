from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from tracybe_app.api.views import lista_instrumento, detalle_instrumento
from tracybe_app.api.views import (CrearTipoEquipo, InstrumentoAV, DetalleInstrumentoAV, SetAV, DetalleSetAV, EmpaqueAV, DetalleEmpaqueAV, BusquedaEmpaqueAV,
                                    TurnoAV, DetalleTurnoAV, EtapaAV, DetalleEtapaAV, AreaSolicitanteAV, DetalleAreaSolicitanteAV, 
                                    EventoLavadoCreate, ListaEventoLavado, DetalleEventoLavado, EventoCreate, ListaEvento, DetalleEvento,
                                    EquipoAV, DetalleEquipoAV, ListaTipoEquipo, DetalleTipoEquipo)



urlpatterns = [
    path('tipoequipo/crear/', CrearTipoEquipo.as_view(), name='tipoequipo-create'),
    path('tipoequipo/', ListaTipoEquipo.as_view(), name='lista-tipoequipo'),
    path('tipoequipo/<int:pk>', DetalleTipoEquipo.as_view(), name = 'tipoequipo-detail'),
    
    path('instrumento/', InstrumentoAV.as_view(), name='lista_instrumento'),
    path('instrumento/<int:pk>', DetalleInstrumentoAV.as_view(), name='instrumento-detail'),
    
    path('set/', SetAV.as_view(), name='lista_set'),
    path('set/<int:pk>', DetalleSetAV.as_view(), name='set-detail'),
    path('empaque/', EmpaqueAV.as_view(), name='lista_empaque'),
    path('empaque/<int:pk>', DetalleEmpaqueAV.as_view(), name='empaque-detail'),
    path('empaque/<str:cadena>', BusquedaEmpaqueAV.as_view(), name='buscarempaque-detail'),
    path('turno/', TurnoAV.as_view(), name='lista_turno'),
    path('turno/<int:pk>', DetalleTurnoAV.as_view(), name='turno-detail'),
    path('etapa/', EtapaAV.as_view(), name='lista_etapa'),
    path('etapa/<int:pk>', DetalleEtapaAV.as_view(), name='etapa-detail'),
    path('areasolicitante/', AreaSolicitanteAV.as_view(), name='lista_turno'),
    path('areasolicitante/<int:pk>', DetalleAreaSolicitanteAV.as_view(), name='areasolicitante-detail'),
    
    path('equipo/', EquipoAV.as_view(), name='lista_equipo'),
    path('equipo/<int:pk>', DetalleEquipoAV.as_view(), name='equipo-detail'),
    
    path('equipo/<int:pk>/eventolavado-create', EventoLavadoCreate.as_view(), name= 'equipoeventolavado-create'),
    path('equipo/<int:pk>/eventolavado/', ListaEventoLavado.as_view(), name='eventolavado-list'),
    path('equipo/eventolavado/<int:pk>', DetalleEventoLavado.as_view(), name='eventolavado-detail'),
    
    path('empaque/<int:pk>/evento-create', EventoCreate.as_view(), name='empaqueevento-create'),
    path('empaque/<int:pk>/evento/', ListaEvento.as_view(), name='empaqueevento-list'),
    path('empaque/evento/<int:pk>', DetalleEvento.as_view(), name='evento-detail'),
]