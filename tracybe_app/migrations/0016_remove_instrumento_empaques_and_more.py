# Generated by Django 5.0 on 2024-04-30 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0015_alter_empaque_materialempaque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='empaques',
        ),
        migrations.DeleteModel(
            name='InstrumentoEmpaque',
        ),
    ]