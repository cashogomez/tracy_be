# Generated by Django 5.0 on 2024-07-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0012_reporteincidencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporteincidencia',
            name='turno',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
