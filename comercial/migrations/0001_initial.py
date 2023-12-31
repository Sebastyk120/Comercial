# Generated by Django 5.0 on 2023-12-18 01:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Contenedor')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Exportador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Fruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Tipo De Caja')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre Cliente')),
                ('direccion', models.CharField(max_length=255, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('tax_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tax ID')),
                ('incoterm', models.CharField(blank=True, max_length=50, null=True, verbose_name='Incoterm')),
                ('agencia_de_carga', models.CharField(blank=True, max_length=100, null=True, verbose_name='Agencia De Carga')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('correo2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo 2')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('intermediario', models.CharField(blank=True, max_length=100, null=True, verbose_name='Intermediario')),
                ('direccion2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direccion 2')),
                ('ciudad2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad 2')),
                ('tax_id2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tax ID2')),
                ('encargado_de_reservar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reservar')),
                ('negociaciones_cartera', models.IntegerField(verbose_name='Dias Cartera')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.pais', verbose_name='Pais')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha Solicitud')),
                ('fecha_entrega', models.DateField(blank=True, null=True, verbose_name='Fecha Entrega')),
                ('dias_cartera', models.IntegerField(blank=True, editable=False, null=True, verbose_name='Dias Cartera')),
                ('awb', models.CharField(blank=True, max_length=50, null=True, verbose_name='AWB')),
                ('destino', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Destino')),
                ('numero_factura', models.CharField(blank=True, max_length=50, null=True, verbose_name='Factura')),
                ('total_cajas_enviadas', models.IntegerField(blank=True, editable=False, null=True, verbose_name='Total Cajas Enviadas')),
                ('nota_credito_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nota credito')),
                ('motivo_nota_credito', models.CharField(blank=True, choices=[('Calidad', 'Calidad'), ('Faltantes', 'Faltantes'), ('Precio', 'Precio')], max_length=20, null=True, verbose_name='Motivo Nota credito')),
                ('valor_total_nota_credito_usd', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10, null=True, verbose_name='Total Nota Credito')),
                ('tasa_representativa_usd_diaria', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='TRM Representativa')),
                ('valor_pagado_cliente_usd', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Pagado Cliente')),
                ('comision_bancaria_usd', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Comision Bancaria USD')),
                ('fecha_pago', models.DateField(blank=True, null=True, verbose_name='Fecha Pago')),
                ('trm_monetizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Monetizacion')),
                ('estado_factura', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Estado Factura')),
                ('diferencia_por_abono', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Diferencia o Abono')),
                ('dias_de_vencimiento', models.IntegerField(blank=True, editable=False, null=True, verbose_name='Dias Vencimiento')),
                ('valor_total_factura_usd', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10, null=True, verbose_name='Valor Total Factura')),
                ('valor_total_comision_usd', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Valor Total Comision USD')),
                ('valor_comision_pesos', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Valor Total Comision Pesos')),
                ('documento_cobro_comision', models.CharField(blank=True, max_length=50, null=True, verbose_name='Documento Cobro Comision')),
                ('fecha_pago_comision', models.DateField(blank=True, null=True, verbose_name='Fecha De Pago Comision')),
                ('estado_comision', models.CharField(editable=False, max_length=50, verbose_name='Estado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.cliente', verbose_name='Cliente')),
                ('exportadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.exportador', verbose_name='Exportador')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Presentacion')),
                ('kilos', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Kilos')),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.fruta', verbose_name='Fruta')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Referencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Referencia')),
                ('referencia_nueva', models.CharField(blank=True, max_length=255, null=True, verbose_name='Referencia Nueva')),
                ('cant_contenedor', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Cajas En Contenedor')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('contenedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comercial.contenedor', verbose_name='Contenedor')),
                ('exportador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.exportador', verbose_name='Exportador')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cajas_solicitadas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cajas Solicitadas')),
                ('presentacion_peso', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=3, null=True, verbose_name='Peso Presentacion')),
                ('kilos', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Kilos')),
                ('cajas_enviadas', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cajas Enviadas')),
                ('kilos_enviados', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Kilos Enviados')),
                ('diferencia', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Diferencia')),
                ('stickers', models.CharField(blank=True, editable=False, null=True, verbose_name='Stikers')),
                ('lleva_contenedor', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], verbose_name='LLeva Contenedor')),
                ('referencia_contenedor', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Referencia Contenedor')),
                ('cantidad_contenedores', models.IntegerField(blank=True, editable=False, null=True, verbose_name='Cantidad Contenedores')),
                ('tarifa_comision', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tarifa Comisión')),
                ('valor_x_caja_usd', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor X Caja USD')),
                ('valor_x_producto', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Valor X Producto')),
                ('no_cajas_nc', models.IntegerField(blank=True, null=True, verbose_name='No Cajas NC')),
                ('valor_nota_credito_usd', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Valor Nota Credito USD')),
                ('afecta_comision', models.BooleanField(blank=True, choices=[(True, 'Sí'), (False, 'No')], null=True, verbose_name='Afecta Comision')),
                ('valor_total_comision_x_producto', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Valor Comision X Producto')),
                ('fruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.fruta', verbose_name='Fruta')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.pedido', verbose_name='Pedido')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.presentacion', verbose_name='Presentacion')),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.referencias', verbose_name='Referencia')),
                ('tipo_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.tipocaja', verbose_name='Tipo De Caja')),
            ],
            options={
                'ordering': ['pedido'],
            },
        ),
    ]
