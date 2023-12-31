from django.contrib import admin
from .models import CotizacionEtnico, CotizacionJuan, CotizacionFieldex
from django.urls import reverse
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin


class CotizacionEtnicoAdmin(SimpleHistoryAdmin):
    list_display = ['presentacion', 'semana'] + ['view_history']

    def view_history(self, obj):
        url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Historial</a>', url)

    view_history.short_description = "Ver Historial"


class CotizacionJuanAdmin(SimpleHistoryAdmin):
    list_display = ['presentacion', 'semana'] + ['view_history']

    def view_history(self, obj):
        url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Historial</a>', url)

    view_history.short_description = "Ver Historial"


class CotizacionFieldexAdmin(SimpleHistoryAdmin):
    list_display = ['presentacion', 'semana'] + ['view_history']

    def view_history(self, obj):
        url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Historial</a>', url)

    view_history.short_description = "Ver Historial"


admin.site.register(CotizacionEtnico, CotizacionEtnicoAdmin)
admin.site.register(CotizacionFieldex, CotizacionFieldexAdmin)
admin.site.register(CotizacionJuan, CotizacionJuanAdmin)
