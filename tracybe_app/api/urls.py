from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from tracybe_app.api.views import lista_instrumento, detalle_instrumento
from tracybe_app.api.views import ( CrearTipoEquipo, DetalleInstrumentoSet, DetalleInstrumentoTicket, DetalleMaterialEmpaqueAV, DetalleSetTicket, DetalleTicketAV, EmpaqueCreate, InstrumentoAV, DetalleInstrumentoAV, InstrumentoSetCreate, InstrumentoSetViewSet, InstrumentoTicketCreate, ListaInstrumentoSet, ListaInstrumentoTicket, ListaSetTicket, MaterialEmpaqueAV, SetAV, DetalleSetAV, EmpaqueAV, DetalleEmpaqueAV, BusquedaEmpaqueAV, SetTicketCreate, TicketAV,
                                    TurnoAV, DetalleTurnoAV, EtapaAV, DetalleEtapaAV, AreaSolicitanteAV, DetalleAreaSolicitanteAV, 
                                    EventoLavadoCreate, ListaEventoLavado, DetalleEventoLavado, EventoCreate, ListaEvento, DetalleEvento,
                                    EquipoAV, DetalleEquipoAV, ListaTipoEquipo, DetalleTipoEquipo)


urlpatterns = [
    
    path('set/<int:pk>/instrumento/<int:ik>/', InstrumentoSetCreate.as_view(), name= 'instrumentoset-create'),
    path('set/<int:pk>/instrumentoset/',ListaInstrumentoSet.as_view(), name='instrumentoset-list'),
    path('set/instrumentoset/<int:pk>', DetalleInstrumentoSet.as_view(), name='instrumentoset-detail'),
    
    path('ticket/<int:pk>/set/<int:ik>/', SetTicketCreate.as_view(), name= 'setticket-create'),
    path('ticket/<int:pk>/set/', ListaSetTicket.as_view(), name='ListaSetTicket-list'),
    path('ticket/set/<int:pk>', DetalleSetTicket.as_view(), name='ticketset-detail'),
    
    path('ticket/<int:pk>/instrumento/<int:ik>/', InstrumentoTicketCreate.as_view(), name= 'instrumentoticket-create'),
    path('ticket/<int:pk>/instrumento/', ListaInstrumentoTicket.as_view(), name='listainstrumentoticket-list'),
    path('ticket/instrumento/<int:pk>', DetalleInstrumentoTicket.as_view(), name='instrumentoticket-detail'),
    
    path('tipoequipo/crear/', CrearTipoEquipo.as_view(), name='tipoequipo-create'),
    path('tipoequipo/', ListaTipoEquipo.as_view(), name='lista-tipoequipo'),
    path('tipoequipo/<int:pk>', DetalleTipoEquipo.as_view(), name = 'tipoequipo-detail'),
    
    path('instrumento/', InstrumentoAV.as_view(), name='lista_instrumento'),
    path('instrumento/<int:pk>', DetalleInstrumentoAV.as_view(), name='instrumento-detail'),
    
    path('set/', SetAV.as_view(), name='lista_set'),
    path('set/<int:pk>', DetalleSetAV.as_view(), name='set-detail'),
    
    path('empaque/', EmpaqueAV.as_view(), name='lista_empaque'),
    path('empaque/materialempaque/<int:pk>/set/<int:ik>', EmpaqueCreate.as_view(), name='crear_empaque'),
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
    
    path('ticket/', TicketAV.as_view(), name='lista_ticket'),
    path('ticket/<int:pk>', DetalleTicketAV.as_view(), name='ticket-detail'),
    
    path('materialempaque/', MaterialEmpaqueAV.as_view(), name='lista-materialempaque'),
    path('materialempaque/<int:pk>', DetalleMaterialEmpaqueAV.as_view(), name = 'materialempaque-detail'),

]