# Generated by Django 5.0 on 2024-06-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridad', models.PositiveSmallIntegerField()),
                ('area_prestamo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('fecha_prestamo', models.DateTimeField(blank=True, default='', max_length=250, null=True)),
                ('recepcion_usuario', models.DateTimeField(blank=True, default='', max_length=250, null=True)),
                ('entrega_usuario', models.DateTimeField(blank=True, default='', max_length=250, null=True)),
                ('notas', models.CharField(blank=True, default='', max_length=900, null=True)),
            ],
        ),
    ]
