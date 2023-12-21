from django.urls import path
from . import views

urlpatterns = [
    path('pedido_detalles/<int:pedido_id>', views.DetallePedidoListView.as_view(), name='pedido_detalle_list'),
    path('pedido_list_general', views.PedidoListView.as_view(), name='pedido_list_general'),
    path('pedido_crear', views.PedidoCreateView.as_view(), name='pedido_crear'),
    path('pedido_editar', views.PedidoUpdateView.as_view(), name='pedido_editar'),
    path('pedido_eliminar', views.PedidoDeleteView.as_view(), name='pedido_eliminar'),
]
