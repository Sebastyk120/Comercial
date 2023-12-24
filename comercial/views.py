from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView
from .forms import SearchForm, PedidoForm, EditarPedidoForm, EliminarPedidoForm, DetallePedidoForm, \
    EliminarDetallePedidoForm
from .models import Pedido, DetallePedido
from .tables import PedidoTable, DetallePedidoTable


# -------------------------------- Tabla De Pedidos General  ----------------------------------------------------
class PedidoListView(SingleTableView):
    model = Pedido
    table_class = PedidoTable
    template_name = 'pedido_list_general.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(cliente__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ----------------------------------- Mostrar Detalles De Pedido General ------------------------------------------
class DetallePedidoListView(SingleTableView):
    model = DetallePedido
    table_class = DetallePedidoTable
    template_name = 'pedido_detalle_list.html'

    def get_queryset(self):
        pedido_id = self.kwargs.get('pedido_id')
        queryset = DetallePedido.objects.filter(pedido__id=pedido_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido_id'] = self.kwargs.get('pedido_id')
        return context


# -------------------------------  Formulario - Crear Pedido General - Modal (General) ----------------------------
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_crear.html'
    success_url = '/pedido_list_general/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()  # Aquí es normal asignar a self.object
        messages.success(self.request,
                         f'El pedido para el cliente {form.cleaned_data['cliente']} se ha creado exitosamente.')
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'html': render_to_string(self.template_name, {'form': form})})


# -------------------------------  Formulario - Editar Pedido General - Modal (General) ----------------------------

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = EditarPedidoForm
    template_name = 'pedido_editar.html'
    success_url = '/pedido_list_general/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        pedido_id = self.request.POST.get('pedido_id')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        return pedido

    def get(self, request, *args, **kwargs):
        pedido_id = request.GET.get('pedido_id')
        self.object = get_object_or_404(Pedido, id=pedido_id)
        formatted_fecha_solicitud = self.object.fecha_solicitud.strftime('%Y-%m-%d')
        formatted_fecha_entrega = self.object.fecha_entrega.strftime('%Y-%m-%d')
        form = self.form_class(
            instance=self.object,
            initial={'fecha_solicitud': formatted_fecha_solicitud, 'fecha_entrega': formatted_fecha_entrega}
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'form': form_html})
        else:
            return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request,
                         f'El pedido para el cliente {form.cleaned_data['cliente']} se ha editado exitosamente.')
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'success': False, 'html': render_to_string(self.template_name, {'form': form}, request=self.request)})
        else:
            return super().form_invalid(form)


# -------------------------------  Formulario - Eliminar Pedido General - Modal (General) ----------------------------

class PedidoDeleteView(UpdateView):
    model = Pedido
    form_class = EliminarPedidoForm
    template_name = 'pedido_eliminar.html'
    success_url = '/pedido_list_general/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        pedido_id = self.request.POST.get('pedido_id')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        return pedido

    def get(self, request, *args, **kwargs):
        pedido_id = request.GET.get('pedido_id')
        self.object = get_object_or_404(Pedido, id=pedido_id)
        formatted_fecha_solicitud = self.object.fecha_solicitud.strftime('%Y-%m-%d')
        formatted_fecha_entrega = self.object.fecha_entrega.strftime('%Y-%m-%d')
        form = self.form_class(
            instance=self.object,
            initial={'fecha_solicitud': formatted_fecha_solicitud, 'fecha_entrega': formatted_fecha_entrega}
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'form': form_html})
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido.delete()
        messages.success(self.request,
                         f'El pedido para el cliente {form.cleaned_data['cliente']} se ha eliminado exitosamente.')
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'success': False, 'html': render_to_string(self.template_name, {'form': form}, request=self.request)})
        else:
            return super().form_invalid(form)


# --------------------------- Formulario Crear  Detalle De Pedido ----------------------------------------------------
class DetallePedidoCreateView(CreateView):
    model = DetallePedido
    form_class = DetallePedidoForm
    template_name = 'detalle_pedido_crear.html'
    success_url = '/detalle_pedido_crear/'

    def get_initial(self):
        initial = super().get_initial()
        pedido_id = self.kwargs.get('pedido_id') or self.request.GET.get('pedido_id')
        if pedido_id:
            initial['pedido'] = pedido_id
        return initial

    @transaction.atomic
    def form_valid(self, form):
        pedido_id = self.kwargs.get('pedido_id')
        if pedido_id:
            pedido = get_object_or_404(Pedido, pk=pedido_id)
            form.instance.pedido = pedido

        self.object = form.save()
        messages.success(self.request, f'El detalle de pedido para el pedido {pedido_id} se ha creado exitosamente.')
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({'success': False, 'error': errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido_id'] = self.kwargs.get('pedido_id')
        return context


# ---------------------------- Formulario Editar Detalle De Pedido --------------------------------------------

class DetallePedidoUpdateView(UpdateView):
    model = DetallePedido
    form_class = DetallePedidoForm
    template_name = 'detalle_pedido_editar.html'
    success_url = '/detalle_pedido_editar/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        detallepedido_id = self.request.POST.get('detallepedido_id')
        detallepedido = get_object_or_404(DetallePedido, id=detallepedido_id)
        return detallepedido

    def get(self, request, *args, **kwargs):
        detallepedido_id = request.GET.get('detallepedido_id')
        self.object = get_object_or_404(DetallePedido, id=detallepedido_id)
        form = self.form_class(
            instance=self.object,
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'form': form_html})
        else:
            return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request,
                         f'El detalle para el {form.cleaned_data['pedido']} se ha editado exitosamente.')
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'success': False, 'html': render_to_string(self.template_name, {'form': form}, request=self.request)})
        else:
            return super().form_invalid(form)


# ---------------------------- Formulario Eliminar Detalle De Pedido --------------------------------------------

class DetallePedidoDeleteiew(UpdateView):
    model = DetallePedido
    form_class = EliminarDetallePedidoForm
    template_name = 'detalle_pedido_eliminart.html'
    success_url = '/detalle_pedido_eliminar/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        detallepedido_id = self.request.POST.get('detallepedido_id')
        detallepedido = get_object_or_404(DetallePedido, id=detallepedido_id)
        return detallepedido

    def get(self, request, *args, **kwargs):
        detallepedido_id = request.GET.get('detallepedido_id')
        self.object = get_object_or_404(DetallePedido, id=detallepedido_id)
        form = self.form_class(
            instance=self.object,
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_html = render_to_string(self.template_name, {'form': form}, request=request)
            return JsonResponse({'form': form_html})
        else:
            return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        detallepedido = form.save(commit=False)
        detallepedido.delete()
        messages.success(self.request,
                         f'El detalle de {form.cleaned_data['pedido']} se ha eliminado exitosamente.')
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'success': False, 'html': render_to_string(self.template_name, {'form': form}, request=self.request)})
        else:
            return super().form_invalid(form)
