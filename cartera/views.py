from django.shortcuts import render, redirect
from django.views import View

from .models import Presentacion, Cotizacion
from .forms import CotizacionForm


class ActualizarCotizacionesView(View):
    form_class = CotizacionForm
    template_name = 'tu_template_actualizar.html'
    semana_actual = 19  # Asegúrate de establecer la semana que deseas cargar

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.get_initial())
        presentaciones_data = []

        for presentacion in Presentacion.objects.all():
            presentaciones_data.append({
                'objeto': presentacion,
                'campo_precio_fob': form[f'precio_fob_{presentacion.id}'],
                'campo_comision_fob': form[f'comision_fob_{presentacion.id}'],
                'campo_precio_dxb': form[f'precio_dxb_{presentacion.id}'],
                'campo_comision_dxb': form[f'comision_dxb_{presentacion.id}']
            })

        return render(request, self.template_name, {
            'form': form,
            'presentaciones_data': presentaciones_data
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        presentaciones = Presentacion.objects.all()
        self.set_form_field_names(presentaciones)

        if form.is_valid():
            self.save_cotizaciones(form)
            return redirect('cotizacion_crear')

        return render(request, self.template_name, {
            'form': form,
            'presentaciones': presentaciones
        })

    def get_initial(self):
        initial_data = {}
        for presentacion in Presentacion.objects.all():
            try:
                cotizacion = Cotizacion.objects.get(presentacion=presentacion, semana=self.semana_actual)
                initial_data[f'precio_fob_{presentacion.id}'] = cotizacion.precio_fob
                initial_data[f'comision_fob_{presentacion.id}'] = cotizacion.comision_fob
                initial_data[f'precio_dxb_{presentacion.id}'] = cotizacion.precio_dxb
                initial_data[f'comision_dxb_{presentacion.id}'] = cotizacion.comision_dxb
            except Cotizacion.DoesNotExist:
                pass
        return initial_data

    def set_form_field_names(self, presentaciones):
        for presentacion in presentaciones:
            presentacion.campo_precio_fob = f'precio_fob_{presentacion.id}'
            presentacion.campo_comision_fob = f'comision_fob_{presentacion.id}'
            presentacion.campo_precio_dxb = f'precio_dxb_{presentacion.id}'
            presentacion.campo_comision_dxb = f'comision_dxb_{presentacion.id}'

    def save_cotizaciones(self, form):
        for presentacion in Presentacion.objects.all():
            cotizacion, created = Cotizacion.objects.get_or_create(
                presentacion=presentacion,
                semana=self.semana_actual
            )
            cotizacion.precio_fob = form.cleaned_data.get(f'precio_fob_{presentacion.id}')
            cotizacion.comision_fob = form.cleaned_data.get(f'comision_fob_{presentacion.id}')
            cotizacion.precio_dxb = form.cleaned_data.get(f'precio_dxb_{presentacion.id}')
            cotizacion.comision_dxb = form.cleaned_data.get(f'comision_dxb_{presentacion.id}')
            cotizacion.save()

