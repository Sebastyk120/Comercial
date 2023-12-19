import django_tables2 as tables

from .models import Movimiento, Item, Inventario


# Ingreso de Referencias (Cajas) Primer momento: --------------------------------------------------------------
class ItemTable(tables.Table):
    editar = tables.TemplateColumn(
        template_name='recibo_editar_button.html',
        orderable=False
    )

    eliminar = tables.TemplateColumn(
        template_name='recibo_eliminar_button.html',
        orderable=False
    )

    class Meta:
        model = Item
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = (
            "numero_item", "cantidad_cajas", "bodega", "proveedor", "fecha_movimiento", "propiedad", "documento",
            "observaciones",
            "user", "editar")


# Historicos (Inventario De Movimientos).---------------------------------------------------------------------------
class MovimientoTable(tables.Table):
    class Meta:
        model = Movimiento
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = (
            "item_historico", "cantidad_cajas_h", "bodega", "propiedad", "fecha_movimiento",
            "observaciones", "fecha", "user",)


class InventarioTable(tables.Table):
    numero_item = tables.Column(verbose_name="Referencia")

    class Meta:
        model = Inventario
        template_name = 'django_tables2/bootstrap5-responsive.html'
        fields = ("numero_item", "compras_efectivas", "saldos_iniciales", "salidas",
                  "traslado_propio", "traslado_remisionado", "ventas", "venta_contenedor")
