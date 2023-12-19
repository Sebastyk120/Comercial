from django.contrib import admin
from .models import Pedido, Fruta, Pais, TipoCaja, Cliente, Presentacion, Contenedor, DetallePedido, Referencias, Exportador


class PedidoAdmin(admin.ModelAdmin):
    # Obtener todos los campos no editables del modelo
    campos_no_editables = [field.name for field in Pedido._meta.fields if not field.editable]
    campos_editables = [field.name for field in Pedido._meta.fields if not field.editable]
    # Crear la lista de visualización agregando 'id' y otros campos no editables
    list_display = ['id'] + campos_no_editables + campos_editables


class DetallePedidoAdmin(admin.ModelAdmin):
    # Obtener todos los campos no editables del modelo
    campos_no_editables = [field.name for field in DetallePedido._meta.fields if not field.editable]
    campos_editables = [field.name for field in DetallePedido._meta.fields if field.editable]
    # Crear la lista de visualización agregando 'id' y otros campos no editables
    list_display = ['id'] + campos_no_editables + campos_editables


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
