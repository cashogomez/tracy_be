# Generated by Django 5.0 on 2024-07-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0010_setticket_entregados'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='devolucion_usuario',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='entrega_usuario',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='recepcion_usuario',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='recepcion_usuario_recepcion',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]