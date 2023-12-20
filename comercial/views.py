from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import SingleTableView
from .forms import SearchForm
from .models import Pedido, DetallePedido
from .tables import PedidoTable, DetallePedidoTable


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


class DetallePedidoListView(SingleTableView):
    model = DetallePedido
    table_class = DetallePedidoTable
    template_name = 'pedido_detalle_list.html'

    def get_queryset(self):
        pedido_id = self.kwargs.get('pedido_id')
        queryset = DetallePedido.objects.filter(pedido__id=pedido_id)
        return queryset
