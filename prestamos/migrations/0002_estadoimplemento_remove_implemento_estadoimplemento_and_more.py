# Generated by Django 5.0.3 on 2024-05-02 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estadoImplemento',
            fields=[
                ('idEstadoImplemento', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEstadoImplemento', models.CharField(max_length=45)),
                ('descripcionEstadoImplemento', models.CharField(max_length=45)),
            ],
        ),
        migrations.RemoveField(
            model_name='implemento',
            name='estadoImplemento',
        ),
        migrations.AddField(
            model_name='implemento',
            name='estadoImplementoId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prestamos.estadoimplemento'),
            preserve_default=False,
        ),
    ]