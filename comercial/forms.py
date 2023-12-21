from django import forms
from django.forms import DateInput
from .models import Pedido, Cliente


class SearchForm(forms.Form):
    item_busqueda = forms.CharField(max_length=256, required=False)


# ------------------------------------ Formulario Crear Pedido ---------------------------------------------
class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Seleccione Un Cliente",
        to_field_name="nombre",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha_solicitud = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    fecha_entrega = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        fecha_solicitud = cleaned_data.get('fecha_solicitud')
        fecha_entrega = cleaned_data.get('fecha_entrega')

        if fecha_entrega and fecha_solicitud and fecha_entrega < fecha_solicitud:
            self.add_error('fecha_entrega', 'La fecha de entrega no puede ser anterior a la fecha de solicitud.')

        return cleaned_data

    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_solicitud', 'fecha_entrega', 'exportadora', 'awb',
                  'numero_factura', 'nota_credito_no', 'motivo_nota_credito']


# ------------------------------------ Formulario Editar Pedido ---------------------------------------------

class EditarPedidoForm(forms.ModelForm):
    fecha_solicitud = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    fecha_entrega = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        fecha_solicitud = cleaned_data.get('fecha_solicitud')
        fecha_entrega = cleaned_data.get('fecha_entrega')

        if fecha_entrega and fecha_solicitud and fecha_entrega < fecha_solicitud:
            self.add_error('fecha_entrega', 'La fecha de entrega no puede ser anterior a la fecha de solicitud.')

        return cleaned_data

    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_solicitud', 'fecha_entrega', 'exportadora', 'awb',
                  'numero_factura', 'nota_credito_no', 'motivo_nota_credito']


# ------------------------------------ Formulario Eliminar Pedido ---------------------------------------------
class EliminarPedidoForm(forms.ModelForm):
    fecha_solicitud = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    fecha_entrega = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_solicitud', 'fecha_entrega', 'exportadora', 'awb',
                  'numero_factura', 'nota_credito_no', 'motivo_nota_credito']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].disabled = True
        self.fields['fecha_solicitud'].disabled = True
        self.fields['fecha_entrega'].disabled = True
        self.fields['exportadora'].disabled = True
        self.fields['awb'].disabled = True
        self.fields['numero_factura'].disabled = True
        self.fields['nota_credito_no'].disabled = True
        self.fields['motivo_nota_credito'].disabled = True
