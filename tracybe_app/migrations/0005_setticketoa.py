# Generated by Django 5.0 on 2024-06-27 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracybe_app', '0004_ticketoa_estatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetTicketOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.set')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracybe_app.ticket')),
            ],
        ),
    ]