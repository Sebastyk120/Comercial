from django import forms
from django.core.validators import MinValueValidator

from .models import Presentacion, CotizacionEtnico


class CotizacionForm(forms.Form):
    SEMANAS_DEL_ANO = [(i, f'Semana {i}') for i in range(1, 53)]
    semana = forms.ChoiceField(choices=SEMANAS_DEL_ANO, required=True)
    trm_cotizacion = forms.DecimalField(validators=[MinValueValidator(0)],
                                        max_digits=10, decimal_places=2,
                                        required=True)

    def __init__(self, *args, **kwargs):
        super(CotizacionForm, self).__init__(*args, **kwargs)

        # Crear campos para cada presentación basado en los campos del modelo Cotizacion
        for presentacion in Presentacion.objects.all():
            for field in CotizacionEtnico._meta.get_fields():
                if hasattr(field, 'max_digits'):  # Verificar si es un campo DecimalField
                    field_name = f"{field.name}_{presentacion.id}"
                    self.fields[field_name] = forms.DecimalField(
                        label=f"{field.verbose_name} - {presentacion.nombre}",
                        max_digits=field.max_digits,
                        decimal_places=field.decimal_places,
                        required=False
                    )


class ComparacionPreciosForm(forms.Form):
    OPCIONES_COMPARACION = [
        ('', 'Seleccione una opción'),
        ('precio_fob', 'precio_fob'),
        ('comi_fob', 'comi_fob'),
        ('precio_dxb', 'precio_dxb'),
        ('comi_dxb', 'comi_dxb'),
        # Agrega más opciones según tus campos
    ]

    presentacion = forms.ModelChoiceField(queryset=Presentacion.objects.all(), required=True)
    semana = forms.IntegerField(min_value=1, max_value=56, required=True)
    tipo_comparacion = forms.ChoiceField(choices=OPCIONES_COMPARACION, required=True)
