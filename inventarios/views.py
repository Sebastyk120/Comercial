from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView
from comercial.models import Referencias
from .forms import ItemForm, SearchForm, EditarItemForm, EliminarItemForm
from .models import Bodega, Item, Movimiento, Inventario
from .tables import MovimientoTable, ItemTable, InventarioTable


# Create your views here.
# Funciones para validar el Grupo del usuario y si puede acceder a la vista:

def es_miembro_del_grupo(nombre_grupo):
    def es_miembro(user):
        return user.groups.filter(name=nombre_grupo).exists()
    return es_miembro

# -------------------------------------- Vistas Para Etnico: ---------------------------------------------------------


# ------------------- Lista de Items Etnico  --------------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Etnico'), login_url=reverse_lazy('home')), name='dispatch')
class ItemListView(SingleTableView):
    model = Item
    table_class = ItemTable
    template_name = 'recibo_items_list_etnico.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(bodega__exportador__nombre='Etnico')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# -------------------------------  Formulario - Crear Item Etnico - Modal (Inventario Real) ----------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Etnico'), login_url=reverse_lazy('home')), name='dispatch')
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'recibo_crear_item_etnico.html'
    success_url = '/recibo_items_create_etnico/'

    def get_initial(self):
        initial = super().get_initial()
        bodega_predeterminada = Bodega.objects.get(nombre='Compras Efectivas', exportador__nombre='Etnico')
        initial['bodega'] = bodega_predeterminada
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar el queryset para mostrar solo las referencias de la exportadora 'Etnico'
        exportadora_etnico = 'Etnico'
        form.fields['numero_item'].queryset = Referencias.objects.filter(exportador__nombre=exportadora_etnico)
        form.fields['bodega'].queryset = Bodega.objects.filter(exportador__nombre=exportadora_etnico)
        return form

    @transaction.atomic
    def form_valid(self, form):
        numero_item = form.cleaned_data['numero_item']
        form.instance.user = self.request.user
        item = form.save()
        Movimiento.objects.create(
            item_historico=item.numero_item,
            cantidad_cajas_h=item.cantidad_cajas,
            bodega=item.bodega,
            propiedad=item.propiedad,
            fecha_movimiento=item.fecha_movimiento,
            observaciones=item.observaciones,
            fecha=timezone.now(),
            user=item.user
        )
        messages.success(self.request, f'El item {numero_item} se ha creado exitosamente.')
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'html': render_to_string(self.template_name, {'form': form})})


# ----------------------------/// Editar Item Recibo  O de ingreso/// ------------------------------------------------

@method_decorator(login_required, name='dispatch')
class ItemUpdateView(UpdateView):
    model = Item
    form_class = EditarItemForm
    template_name = 'recibo_editar_item.html'
    success_url = '/update_items/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        item_id = self.request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        return item

    def get(self, request, *args, **kwargs):
        item_id = request.GET.get('item_id')
        self.object = get_object_or_404(Item, id=item_id)
        formatted_fecha_movimiento = self.object.fecha_movimiento.strftime('%Y-%m-%d')
        form = self.form_class(
            instance=self.object,
            initial={'fecha_movimiento': formatted_fecha_movimiento}
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
        form.instance.user = self.request.user
        numero_item = form.cleaned_data['numero_item']
        item = form.save()
        Movimiento.objects.create(
            item_historico=item.numero_item,
            cantidad_cajas_h=item.cantidad_cajas,
            bodega=item.bodega,
            propiedad=item.propiedad,
            fecha_movimiento=item.fecha_movimiento,
            observaciones=item.observaciones,
            fecha=timezone.now(),
            user=item.user
        )
        messages.success(self.request, f'El item {numero_item} se ha editado exitosamente.')
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


# ----------------------------/// Eliminar Item Recibo  O de ingreso/// ------------------------------------------------
@method_decorator(login_required, name='dispatch')
class ItemDeleteView(UpdateView):
    model = Item
    form_class = EliminarItemForm
    template_name = 'recibo_eliminar_item.html'
    success_url = '/recibo_items_delete/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_object(self, queryset=None):
        item_id = self.request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        return item

    def get(self, request, *args, **kwargs):
        item_id = request.GET.get('item_id')
        self.object = get_object_or_404(Item, id=item_id)
        form = self.form_class(instance=self.object)
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
        form.instance.user = self.request.user
        numero_item = form.cleaned_data['numero_item']
        item = form.save()
        item.delete()
        Movimiento.objects.create(
            item_historico=item.numero_item,
            cantidad_cajas_h=item.cantidad_cajas,
            bodega=item.bodega,
            propiedad=item.propiedad,
            fecha_movimiento=item.fecha_movimiento,
            observaciones=item.observaciones,
            fecha=timezone.now(),
            user=item.user
        )
        messages.success(self.request, f'El item {numero_item} se ha eliminado exitosamente.')
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


# -------------------------------------- Vistas Para Fieldex: ---------------------------------------------------------
# ------------------- Lista de Items Fieldex  --------------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Fieldex'), login_url=reverse_lazy('home')), name='dispatch')
class ItemListViewFieldex(SingleTableView):
    model = Item
    table_class = ItemTable
    template_name = 'recibo_items_list_fieldex.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(bodega__exportador__nombre='Fieldex')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ---------------------------- //// Crear Item Fieldex (Ingreso) //////////////////----------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Fieldex'), login_url=reverse_lazy('home')), name='dispatch')
class ItemCreateViewFieldex(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'recibo_crear_item_fieldex.html'
    success_url = '/recibo_items_create_fieldex/'

    def get_initial(self):
        initial = super().get_initial()
        bodega_predeterminada = Bodega.objects.get(nombre='Compras Efectivas', exportador__nombre='Fieldex')
        initial['bodega'] = bodega_predeterminada
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar el queryset para mostrar solo las referencias de la exportadora 'Fieldex'
        exportadora_etnico = 'Fieldex'
        form.fields['numero_item'].queryset = Referencias.objects.filter(exportador__nombre=exportadora_etnico)
        form.fields['bodega'].queryset = Bodega.objects.filter(exportador__nombre=exportadora_etnico)
        return form

    @transaction.atomic
    def form_valid(self, form):
        numero_item = form.cleaned_data['numero_item']
        form.instance.user = self.request.user
        item = form.save()
        Movimiento.objects.create(
            item_historico=item.numero_item,
            cantidad_cajas_h=item.cantidad_cajas,
            bodega=item.bodega,
            propiedad=item.propiedad,
            fecha_movimiento=item.fecha_movimiento,
            observaciones=item.observaciones,
            fecha=timezone.now(),
            user=item.user
        )
        messages.success(self.request, f'El item {numero_item} se ha creado exitosamente.')
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'html': render_to_string(self.template_name, {'form': form})})


# -------------------------------------- Vistas Para Juan Matas--------------------------------------------------------


# Mostrar Tabla Recibo - Bodega Recibo Juan Matas (Mostrar Items de ingreso)
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Juan_Matas'), login_url=reverse_lazy('home')), name='dispatch')
class ItemListViewJuan(SingleTableView):
    model = Item
    table_class = ItemTable
    template_name = 'recibo_items_list_juan.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(bodega__exportador__nombre='Juan_Matas')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ---------------------------- //// Crear Item Juan Matas (Ingreso) //////////////////----------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Juan_Matas'), login_url=reverse_lazy('home')), name='dispatch')
class ItemCreateViewJuan(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'recibo_crear_item_juan.html'
    success_url = '/recibo_items_create_juan/'

    def get_initial(self):
        initial = super().get_initial()
        bodega_predeterminada = Bodega.objects.get(nombre='Compras Efectivas', exportador__nombre='Juan_Matas')
        initial['bodega'] = bodega_predeterminada
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar el queryset para mostrar solo las referencias de la exportadora 'Fieldex'
        exportadora_etnico = 'Juan_Matas'
        form.fields['numero_item'].queryset = Referencias.objects.filter(exportador__nombre=exportadora_etnico)
        form.fields['bodega'].queryset = Bodega.objects.filter(exportador__nombre=exportadora_etnico)
        return form

    @transaction.atomic
    def form_valid(self, form):
        numero_item = form.cleaned_data['numero_item']
        form.instance.user = self.request.user
        item = form.save()
        Movimiento.objects.create(
            item_historico=item.numero_item,
            cantidad_cajas_h=item.cantidad_cajas,
            bodega=item.bodega,
            propiedad=item.propiedad,
            fecha_movimiento=item.fecha_movimiento,
            observaciones=item.observaciones,
            fecha=timezone.now(),
            user=item.user
        )
        messages.success(self.request, f'El item {numero_item} se ha creado exitosamente.')
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'html': render_to_string(self.template_name, {'form': form})})


# -----------------------------------// Tabla General Para Historico de Movimientos----------------------------------//


# Tabla De Historico De Movimientos. (Movimientos Inventario General)
class MovimientoListView(SingleTableView):
    model = Movimiento
    table_class = MovimientoTable
    template_name = 'historico.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            item_busqueda = form.cleaned_data.get('item_busqueda')
            if item_busqueda:
                queryset = queryset.filter(item_historico__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ----------------------- ///  Lista De Inventarios Por Bodega /// ----------------------------------------------

# ----------------------- ///  Lista De Inventarios Por Etnico /// ----------------------------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Etnico'), login_url=reverse_lazy('home')), name='dispatch')
class InventarioBodegaEtnicoListView(SingleTableView):
    model = Inventario
    table_class = InventarioTable
    template_name = 'inventario_list_bodega_etnico.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(numero_item__exportador__nombre='Etnico')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ----------------------- ///  Lista De Inventarios Por Fieldex /// ----------------------------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Fieldex'), login_url=reverse_lazy('home')), name='dispatch')
class InventarioBodegaFieldexListView(SingleTableView):
    model = Inventario
    table_class = InventarioTable
    template_name = 'inventario_list_bodega_fieldex.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(numero_item__exportador__nombre='Fieldex')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ----------------------- ///  Lista De Inventarios Por Juan Matas /// ----------------------------------------------
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(es_miembro_del_grupo('Juan_Matas'), login_url=reverse_lazy('home')), name='dispatch')
class InventarioBodegaJuanListView(SingleTableView):
    model = Inventario
    table_class = InventarioTable
    template_name = 'inventario_list_bodega_juan.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(numero_item__exportador__nombre='Juan_Matas')
        form = self.form_class(self.request.GET)
        if form.is_valid() and form.cleaned_data.get('item_busqueda'):
            item_busqueda = form.cleaned_data.get('item_busqueda')
            queryset = queryset.filter(numero_item__nombre__icontains=item_busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_busqueda'] = self.form_class(self.request.GET)
        return context


# ------------------------- /////// Tabla totalizada por bodega //////////// ------------------------------------------
