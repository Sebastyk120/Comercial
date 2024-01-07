from django.urls import path
from . import views

urlpatterns = [
    path('pedido_detalles/<int:pedido_id>', views.DetallePedidoListView.as_view(), name='pedido_detalle_list'),
    path('pedido_list_general', views.PedidoListView.as_view(), name='pedido_list_general'),
    path('pedido_crear', views.PedidoCreateView.as_view(), name='pedido_crear'),
    path('pedido_editar', views.PedidoUpdateView.as_view(), name='pedido_editar'),
    path('pedido_eliminar', views.PedidoDeleteView.as_view(), name='pedido_eliminar'),
    path('detalle_pedido_crear/<int:pedido_id>', views.DetallePedidoCreateView.as_view(), name='detalle_pedido_crear'),
    path('detalle_pedido_editar', views.DetallePedidoUpdateView.as_view(), name='detalle_pedido_editar'),
    path('detalle_pedido_eliminar', views.DetallePedidoDeleteiew.as_view(), name='detalle_pedido_eliminar'),
    path('pedido_list_etnico', views.PedidoEtnicoListView.as_view(), name='pedido_list_etnico'),
    path('pedido_list_fieldex', views.PedidoFieldexListView.as_view(), name='pedido_list_fieldex'),
    path('pedido_list_juan', views.PedidoJuanListView.as_view(), name='pedido_list_juan'),
    path('pedido_editar_exportador', views.PedidoExportadorUpdateView.as_view(), name='pedido_editar_exportador'),
    path('cartera_list_heavens', views.CarteraHeavensListView.as_view(), name='cartera_list_heavens'),
    path('cartera_list_etnico', views.CarteraEtnicoListView.as_view(), name='cartera_list_etnico'),
    path('cartera_list_fieldex', views.CarteraFieldexListView.as_view(), name='cartera_list_fieldex'),
    path('cartera_list_juan', views.CarteraJuanListView.as_view(), name='cartera_list_juan'),
    path('exportar_cartera_clientes', views.export_cartera_clientes, name='exportar_cartera_clientes'),
    path('exportar_cartera_etnico', views.export_cartera_etnico, name='exportar_cartera_etnico'),
    path('exportar_cartera_fieldex', views.export_cartera_fieldex, name='exportar_cartera_fieldex'),
    path('exportar_cartera_juan', views.export_cartera_juan, name='exportar_cartera_juan'),
]
