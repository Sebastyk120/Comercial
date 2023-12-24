from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Pedido, Fruta, Pais, TipoCaja, Cliente, Presentacion, Contenedor, DetallePedido, Referencias, \
    Exportador
from simple_history.admin import SimpleHistoryAdmin


class PedidoAdmin(SimpleHistoryAdmin):
    # Tus campos existentes
    campos_no_editables = [field.name for field in Pedido._meta.fields if not field.editable]
    campos_editables = [field.name for field in Pedido._meta.fields if field.editable]

    # Crear la lista de visualización agregando 'id', campos no editables y editables
    list_display = ['id'] + campos_no_editables + campos_editables + ['view_history']

    def view_history(self, obj):
        url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Historial</a>', url)

    view_history.short_description = "Ver Historial"


class DetallePedidoAdmin(admin.ModelAdmin):
    # Obtener todos los campos no editables del modelo
    campos_no_editables = [field.name for field in DetallePedido._meta.fields if not field.editable]
    campos_editables = [field.name for field in DetallePedido._meta.fields if field.editable]
    # Crear la lista de visualización agregando 'id' y otros campos no editables
    list_display = ['id'] + campos_no_editables + campos_editables + ['view_history']

    def view_history(self, obj):
        url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Historial</a>', url)

    view_history.short_description = "Ver Historial"


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Fruta)
admin.site.register(Pais)
admin.site.register(TipoCaja)
admin.site.register(Cliente)
admin.site.register(Presentacion)
admin.site.register(Contenedor)
admin.site.register(DetallePedido, DetallePedidoAdmin)
admin.site.register(Referencias)
admin.site.register(Exportador)
