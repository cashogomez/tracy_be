from django.contrib import admin
from tracybe_app.models import (EventoEsterilizacion, Instrumento, MaterialEmpaque, MaterialEnEsterilizador, ReporteIncidencia, Set, Empaque, SetTicketOA, TicketOA, Turno, Etapa, Evento, AreaSolicitante, 
                                Equipo, EventoLavado, Ciclo,  Estatus, Paciente, Ticket,
                                InstrumentoSet,  SetEmpaque, SetTicket, InstrumentoTicket, CiclosEquipo)
# Register your models here.
admin.site.register(AreaSolicitante)
admin.site.register(Turno)
admin.site.register(Etapa)
admin.site.register(Empaque)
admin.site.register(Set)
admin.site.register(Evento)
admin.site.register(Estatus)
admin.site.register(Ciclo)
admin.site.register(Equipo)
admin.site.register(Instrumento)
admin.site.register(EventoLavado)
admin.site.register(Paciente)
admin.site.register(Ticket)
admin.site.register(InstrumentoSet)
admin.site.register(SetEmpaque)
admin.site.register(SetTicket)
admin.site.register(InstrumentoTicket)
admin.site.register(MaterialEmpaque)
admin.site.register(CiclosEquipo)
admin.site.register(MaterialEnEsterilizador)
admin.site.register(EventoEsterilizacion)
admin.site.register(TicketOA)
admin.site.register(SetTicketOA)
admin.site.register(ReporteIncidencia)



