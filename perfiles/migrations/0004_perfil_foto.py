# Generated by Django 5.0 on 2024-01-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_areatrabajo_puesto_perfil_empresa_id_perfil_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
