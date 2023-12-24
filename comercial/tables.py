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
