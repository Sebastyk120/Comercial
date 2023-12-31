# Generated by Django 5.0 on 2023-12-27 05:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comercial', '0006_alter_historicalpedido_tasa_representativa_usd_diaria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('comision_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('comision_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.presentacion')),
            ],
        ),
    ]
