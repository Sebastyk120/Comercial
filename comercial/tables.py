import django_tables2 as tables
from django.utils.html import format_html

from .models import Pedido, DetallePedido


class PedidoTable(tables.Table):
    detalle = tables.TemplateColumn(
        template_name='detalle_pedido_button.html',
        orderable=False
    )

    editar = tables.TemplateColumn(
        template_name='editar_pedido_button.html',
        orderable=False
    )

    eliminar = tables.TemplateColumn(
        template_name='eliminar_pedido_button.html',
        orderable=False
    )

    class Meta:
        model = Pedido
        template_name = "django_tables2/bootstrap5-responsive.html"


class DetallePedidoTable(tables.Table):
    editar = tables.TemplateColumn(
        template_name='detalle_pedido_editar_button.html',
        orderable=False
    )

    eliminar = tables.TemplateColumn(
        template_name='detalle_pedido_eliminar_button.html',
        orderable=False
    )

    class Meta:
        model = DetallePedido
        template_name = "django_tables2/bootstrap5-responsive.html"
        exclude = ("pedido", "id")


class PedidoExportadorTable(tables.Table):
    detalle = tables.TemplateColumn(
        template_name='detalle_pedido_button.html',
        orderable=False
    )

    editar = tables.TemplateColumn(
        template_name='editar_pedido_button.html',
        orderable=False
    )

    class Meta:
        model = Pedido
        template_name = "django_tables2/bootstrap5-responsive.html"


class CarteraPedidoTable(tables.Table):
    fecha_entrega_personalizada = tables.DateColumn(
        accessor='fecha_entrega',
        verbose_name='Fecha Factura'
    )

    class Meta:
        model = Pedido
        template_name = "django_tables2/bootstrap5-responsive.html"
        order_by = ('cliente',)
        fields = (
            "id", "cliente", "exportadora", "numero_factura", "fecha_entrega_personalizada", "dias_de_vencimiento",
            "valor_total_factura_usd", "valor_pagado_cliente_usd", "comision_bancaria_usd", "fecha_pago",
            "estado_factura")


class ComisionPedidoTable(tables.Table):
    fecha_entrega_personalizada = tables.DateColumn(
        accessor='fecha_pago',
        verbose_name='Fecha Pago Cliente'
    )
    cobro_comision = tables.BooleanColumn(orderable=False, verbose_name="Cobro Comisión")

    class Meta:
        model = Pedido
        template_name = "django_tables2/bootstrap5-responsive.html"
        order_by = ('cliente',)
        fields = ("id", "cobro_comision",
                  "cliente", "exportadora", "fecha_entrega_personalizada", "valor_total_factura_usd",
                  "diferencia_por_abono",
                  "trm_monetizacion", "estado_factura", "valor_total_comision_usd", "valor_comision_pesos",
                  "documento_cobro_comision", "fecha_pago_comision", "estado_comision")

    def render_cobro_comision(self, record):
        if record.diferencia_por_abono >= 0:
            return format_html('<span style="color: green;">✔️</span>')
        else:
            return format_html('<span style="color: red;">❌</span>')
