from django.urls import path
from . import views

urlpatterns = [
    path('historico_items', views.MovimientoListView.as_view(), name='historicos'),
    path('inventario_bodega_etnico', views.InventarioBodegaEtnicoListView.as_view(), name='inventario_bodega_etnico'),
    path('inventario_bodega_fieldex', views.InventarioBodegaFieldexListView.as_view(), name='inventario_bodega_fieldex'),
    path('inventario_bodega_juan', views.InventarioBodegaJuanListView.as_view(), name='inventario_bodega_juan'),
    path('recibo_items_list_etnico', views.ItemListView.as_view(), name='reciboitemslistetnico'),
    path('recibo_items_create_etnico', views.ItemCreateView.as_view(), name='reciboitemscreateetnico'),
    path('recibo_items_create_fieldex', views.ItemCreateViewFieldex.as_view(), name='reciboitemscreatefieldex'),
    path('recibo_items_list_fieldex', views.ItemListViewFieldex.as_view(), name='reciboitemslistfieldex'),
    path('recibo_items_list_juan', views.ItemListViewJuan.as_view(), name='reciboitemslistjuan'),
    path('recibo_items_create_juan', views.ItemCreateViewJuan.as_view(), name='reciboitemscreatejuan'),
    path('recibo_items_update', views.ItemUpdateView.as_view(), name='reciboitemsupdate'),
    path('recibo_items_delete', views.ItemDeleteView.as_view(), name='reciboitemsdelete'),
]
