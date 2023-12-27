from django import forms
from .models import Presentacion, Cotizacion


class CotizacionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CotizacionForm, self).__init__(*args, **kwargs)
        for presentacion in Presentacion.objects.all():
            # Crear campos para cada presentación
            self.fields[f'precio_fob_{presentacion.id}'] = forms.DecimalField(
                label=f"Precio FOB - {presentacion.nombre}",
                max_digits=10,
                decimal_places=2,
                required=False
            )
            self.fields[f'comision_fob_{presentacion.id}'] = forms.DecimalField(
                label=f"Comisión FOB - {presentacion.nombre}",
                max_digits=10,
                decimal_places=2,
                required=False
            )
            self.fields[f'precio_dxb_{presentacion.id}'] = forms.DecimalField(
                label=f"Precio DXB - {presentacion.nombre}",
                max_digits=10,
                decimal_places=2,
                required=False
            )
            self.fields[f'comision_dxb_{presentacion.id}'] = forms.DecimalField(
                label=f"Comisión DXB - {presentacion.nombre}",
                max_digits=10,
                decimal_places=2,
                required=False
            )
