# Generated by Django 5.0 on 2024-05-09 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0018_alter_empaque_materialempaque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='ciclos',
        ),
        migrations.CreateModel(
            name='CiclosEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.ciclo')),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.equipo')),
            ],
        ),
        migrations.AddField(
            model_name='ciclo',
            name='equipos',
            field=models.ManyToManyField(through='tracybe_app.CiclosEquipo', to='tracybe_app.equipo'),
        ),
    ]