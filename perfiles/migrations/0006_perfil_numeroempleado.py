# Generated by Django 5.0 on 2024-01-31 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0005_alter_perfil_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='numeroEmpleado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
