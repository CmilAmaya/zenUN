# Generated by Django 5.0.3 on 2024-06-12 01:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_evento_fechahoraeventofinal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalevento',
            name='flyer',
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaHoraEventoFinal',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 21, 31, 17, 563912)),
        ),
        migrations.AlterField(
            model_name='historicalevento',
            name='fechaHoraEventoFinal',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 21, 31, 17, 563912)),
        ),
    ]
