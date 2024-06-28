# Generated by Django 5.0 on 2024-06-20 01:29

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSolicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('duracion', models.TimeField(default=datetime.time(8, 0))),
                ('temperatura', models.IntegerField(blank=True, default=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizados', models.IntegerField(blank=True, default=0, null=True)),
                ('codigo_qr', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('familia', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('individuo', models.IntegerField(blank=True, default=0, null=True)),
                ('tipo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('marca', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('lote', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('foto', models.URLField(blank=True, default='', max_length=250, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('uso', models.IntegerField(blank=True, default=0, null=True)),
                ('codigo_qr', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('prelavado', models.BooleanField(default=False)),
                ('completo', models.BooleanField(default=True)),
                ('funcional', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialEmpaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('marca', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tiempo_vida', models.IntegerField(blank=True, default=0, null=True)),
                ('unidad', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialEnEsterilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_esterilizador', models.IntegerField(blank=True, default=0, null=True)),
                ('setId', models.IntegerField(blank=True, default=0, null=True)),
                ('nombreSet', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('turno', models.IntegerField(blank=True, default=0, null=True)),
                ('eventoesterilizador', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('paterno', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('materno', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, default='2021-12-31 15:25:00+01', null=True)),
                ('numero_habitacion', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('diagnostico', models.CharField(blank=True, default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(default=0, null=True)),
                ('maximo', models.PositiveIntegerField(default=0, null=True)),
                ('minimo', models.PositiveIntegerField(default=0, null=True)),
                ('nombre', models.CharField(max_length=250)),
                ('foto', models.URLField(blank=True, default='', max_length=250, null=True)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cirugia', models.DateTimeField(blank=True, default='', max_length=250, null=True)),
                ('habitacion', models.IntegerField(blank=True, default=0, null=True)),
                ('paciente', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('sala', models.IntegerField(blank=True, default=0, null=True)),
                ('turno', models.IntegerField(blank=True, default=0, null=True)),
                ('registro', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('edad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, default='', max_length=250, null=True)),
                ('diagnostico', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('cirugia', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('solicita', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('cirujano', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('anestesiologo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('anestesia', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('residente', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('area_registro', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('enfermero', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('prioridad', models.PositiveSmallIntegerField()),
                ('estatus', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('notas', models.CharField(blank=True, default='', max_length=900, null=True)),
                ('activo', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0)),
                ('inicio', models.TimeField(default=datetime.time(8, 0))),
                ('fin', models.TimeField(default=datetime.time(15, 0))),
            ],
        ),
        migrations.CreateModel(
            name='CiclosEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('estatus', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('marca', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('modelo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('numero_serie', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('ciclos', models.ManyToManyField(through='tracybe_app.CiclosEquipo', to='tracybe_app.ciclo')),
            ],
        ),
        migrations.AddField(
            model_name='ciclosequipo',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.equipo'),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folioPBD', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('folioPB', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('folioPQ', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('incidencia', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('notas', models.CharField(blank=True, default='', max_length=900, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('devolvio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listadevolvioevento', to=settings.AUTH_USER_MODEL)),
                ('empaque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaempaqueevento', to='tracybe_app.empaque')),
                ('entrego', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaentregoevento', to=settings.AUTH_USER_MODEL)),
                ('etapa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaetapaevento', to='tracybe_app.etapa')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaperfilevento', to=settings.AUTH_USER_MODEL)),
                ('recepciono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listarecepcionoevento', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventoEsterilizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_esterilizador', models.IntegerField(blank=True, default=0, null=True)),
                ('perfil_inicio', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('hora_inicio', models.TimeField(blank=True, default='', max_length=250, null=True)),
                ('fecha_inicio', models.CharField(blank=True, null=True)),
                ('perfil_final', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('hora_final', models.TimeField(blank=True, default='', max_length=250, null=True)),
                ('fecha_final', models.CharField(blank=True, null=True)),
                ('cicloDiario', models.IntegerField(blank=True, default=0, null=True)),
                ('ciclo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cicloEventoEsterilizacion', to='tracybe_app.ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='EventoLavado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.TimeField(default=datetime.time(8, 0))),
                ('inicio', models.BooleanField(default=False)),
                ('paro', models.BooleanField(default=False)),
                ('finalizado', models.BooleanField(default=False)),
                ('incidencia', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaequipoeventolavado', to='tracybe_app.equipo')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listaperfileventolavado', to=settings.AUTH_USER_MODEL)),
                ('instrumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listainstrumentoeventolavado', to='tracybe_app.instrumento')),
            ],
        ),
        migrations.AddField(
            model_name='empaque',
            name='materialempaque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materialempaque', to='tracybe_app.materialempaque'),
        ),
        migrations.CreateModel(
            name='InstrumentoSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('instrumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.instrumento')),
                ('set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.set')),
            ],
        ),
        migrations.AddField(
            model_name='instrumento',
            name='sets',
            field=models.ManyToManyField(through='tracybe_app.InstrumentoSet', to='tracybe_app.set'),
        ),
        migrations.CreateModel(
            name='SetEmpaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('empaque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.empaque')),
                ('set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.set')),
            ],
        ),
        migrations.AddField(
            model_name='set',
            name='empaques',
            field=models.ManyToManyField(through='tracybe_app.SetEmpaque', to='tracybe_app.empaque'),
        ),
        migrations.CreateModel(
            name='SetTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.set')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.ticket')),
            ],
        ),
        migrations.AddField(
            model_name='set',
            name='tickets',
            field=models.ManyToManyField(through='tracybe_app.SetTicket', to='tracybe_app.ticket'),
        ),
        migrations.CreateModel(
            name='InstrumentoTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('instrumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.instrumento')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.ticket')),
            ],
        ),
        migrations.AddField(
            model_name='instrumento',
            name='tickets',
            field=models.ManyToManyField(through='tracybe_app.InstrumentoTicket', to='tracybe_app.ticket'),
        ),
    ]
