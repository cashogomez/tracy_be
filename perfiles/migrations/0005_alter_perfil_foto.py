# Generated by Django 5.0 on 2024-01-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
