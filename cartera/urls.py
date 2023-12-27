from django.urls import path
from . import views

urlpatterns = [
    path('cotizacion_crear', views.ActualizarCotizacionesView.as_view(), name='cotizacion_crear'),
]
