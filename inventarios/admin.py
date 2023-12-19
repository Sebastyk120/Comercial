from django.contrib import admin
from .models import Bodega, Item, Movimiento, Inventario, Proveedor


class MovimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)


admin.site.register(Bodega)
admin.site.register(Item)
admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(Inventario)
admin.site.register(Proveedor)
