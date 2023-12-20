from django.urls import path
from .views import PedidoListView, DetallePedidoListView  # Importa las vistas

urlpatterns = [
    path('pedido_list_general/', PedidoListView.as_view(), name='pedido_list_general'),
    path('pedido/<int:pedido_id>/detalles/', DetallePedidoListView.as_view(), name='pedido_detalle_list'),
]
