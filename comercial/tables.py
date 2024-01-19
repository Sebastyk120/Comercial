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

    inf = tables.TemplateColumn(
        template_name='resumen_pedido_button.html',
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
        fields = ["fruta", "presentacion", "cajas_solicitadas", "presentacion_peso", "kilos", "cajas_enviadas",
                  "kilos_enviados", "diferencia", "tipo_caja", "referencia__nombre", "stickers", "lleva_contenedor",
                  "referencia_contenedor", "cantidad_contenedores", "tarifa_comision", "valor_x_caja_usd",
                  "valor_x_caja_usd", "valor_x_producto", "no_cajas_nc", "valor_nota_credito_usd", "afecta_comision",
                  "valor_total_comision_x_producto", "precio_proforma", "observaciones"]
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

    inf = tables.TemplateColumn(
        template_name='resumen_pedido_button.html',
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


class ResumenPedidoTable(tables.Table):
    peso_bruto = tables.Column(empty_values=(), orderable=False, verbose_name="Peso Bruto")
    cajas_solicitadas = tables.Column(verbose_name="Cajas Pedido")
    lleva_contenedor = tables.BooleanColumn(orderable=False, verbose_name="Contenedor")
    valor_x_caja_usd = tables.Column(verbose_name="$Precio Final")
    tarifa_comision = tables.Column(verbose_name="$Comisión Caja")
    precio_proforma = tables.Column(verbose_name="$Proforma")
    precio_und_caja = tables.Column(empty_values=(), orderable=False, verbose_name="$Precio Caja")

    class Meta:
        model = DetallePedido
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ["fruta", "presentacion", "cajas_solicitadas", "presentacion_peso", "kilos", "peso_bruto", "tipo_caja",
                  "referencia__nombre", "stickers", "lleva_contenedor", "observaciones", "precio_und_caja",
                  "tarifa_comision", "valor_x_caja_usd", "precio_proforma"]
        exclude = ("pedido", "id")

    def render_peso_bruto(self, record):
        return record.calcular_peso_bruto()

    def render_lleva_contenedor(self, record):
        if record.lleva_contenedor is True:
            return format_html('<span style="color: green;">✔</span>')
        else:
            return format_html('<span style="color: red;">❌</span>')

    def render_precio_und_caja(self, record):
        return record.valor_x_caja_usd - record.tarifa_comision
