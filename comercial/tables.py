import django_tables2 as tables
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
        order_by = ('cliente__nombre',)
        fields = ("cliente", "numero_factura", "fecha_entrega_personalizada", "dias_de_vencimiento",
                  "valor_total_factura_usd", "valor_pagado_cliente_usd", "fecha_pago", "estado_factura")
