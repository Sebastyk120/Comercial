import logging
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.http import request
from comercial.models import Referencias, Exportador


class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    exportador = models.ForeignKey(Exportador, on_delete=models.CASCADE, verbose_name="Exportador")

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.exportador} "


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Proveedor")

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}"


class Item(models.Model):
    numero_item = models.ForeignKey(Referencias, verbose_name="Referencia", on_delete=models.CASCADE)
    cantidad_cajas = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad Cajas")
    documento = models.CharField(max_length=100, verbose_name="Documento", blank=True, null=True)
    bodega = models.ForeignKey(Bodega, verbose_name="Bodega", on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")
    fecha_movimiento = models.DateField(verbose_name="Fecha Movimiento")
    propiedad = models.ForeignKey(Exportador, on_delete=models.CASCADE, verbose_name="Propiedad")
    observaciones = models.CharField(verbose_name="Observaciones", blank=True, null=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return (f"Referencia: {self.numero_item} -Bodega: {self.bodega} -Cantidad {self.cantidad_cajas} "
                f"- {self.fecha_movimiento}")


class Movimiento(models.Model):
    item_historico = models.CharField(max_length=100)
    cantidad_cajas_h = models.IntegerField(verbose_name="Cantidad Cajas")
    bodega = models.ForeignKey(Bodega, verbose_name="Bodega", on_delete=models.CASCADE)
    propiedad = models.CharField(max_length=50, verbose_name="Propiedad")
    fecha_movimiento = models.DateField(verbose_name="Fecha Movimiento")
    observaciones = models.CharField(verbose_name="Observaciones", blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Historico")
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name="Usuario")

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.item_historico} - {self.cantidad_cajas_h} - {self.bodega} - {self.fecha}"


class Inventario(models.Model):
    numero_item = models.ForeignKey(Referencias, verbose_name="Referencia", on_delete=models.CASCADE)
    compras_efectivas = models.IntegerField(default=0, verbose_name="Compras Efectivas", blank=True, null=True)
    saldos_iniciales = models.IntegerField(default=0, verbose_name="Saldos Iniciales", blank=True, null=True)
    salidas = models.IntegerField(default=0, verbose_name="Salidas", blank=True, null=True)
    traslado_propio = models.IntegerField(default=0, verbose_name="Traslado Propio", blank=True, null=True)
    traslado_remisionado = models.IntegerField(default=0, verbose_name="Traslado Remisionado", blank=True, null=True)
    ventas = models.IntegerField(default=0, verbose_name="Ventas", blank=True, null=True)

    class Meta:
        ordering = ['numero_item']

    def __str__(self):
        return f"{self.numero_item.nombre} - {self.numero_item.exportador.nombre}"


# Señal para actualizar automáticamente el modelo Inventario después de guardar o borrar un objeto Item
@receiver(post_save, sender=Item)
def actualizar_inventario_al_guardar(sender, instance, **kwargs):
    item = instance.numero_item
    bodega = instance.bodega
    nuevo_inventario, created = Inventario.objects.get_or_create(
        numero_item=instance.numero_item,
        defaults={'compras_efectivas': 0, 'saldos_iniciales': 0, 'salidas': 0, 'traslado_propio': 0,
                  'traslado_remisionado': 0, 'ventas': 0}
    )
    if bodega.nombre == 'Compras Efectivas':
        nuevo_inventario.compras_efectivas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Saldos Iniciales':
        nuevo_inventario.saldos_iniciales = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Salidas':
        nuevo_inventario.salidas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Traslado Propio':
        nuevo_inventario.traslado_propio = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Traslado Remisionado':
        nuevo_inventario.traslado_remisionado = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Ventas':
        nuevo_inventario.ventas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    else:
        # Manejo de error y envío de alerta
        logging.error(f"Condición no manejada para la bodega: {item.bodega.nombre}")
        messages.error(request, f"Condición no manejada para la bodega: {item.bodega.nombre}")


@receiver(post_delete, sender=Item)
def actualizar_inventario_al_eliminar(sender, instance, **kwargs):
    item = instance.numero_item
    bodega = instance.bodega
    nuevo_inventario = Inventario.objects.get(
        numero_item=instance.numero_item,
    )
    if bodega.nombre == 'Compras Efectivas':
        nuevo_inventario.compras_efectivas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Saldos Iniciales':
        nuevo_inventario.saldos_iniciales = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Salidas':
        nuevo_inventario.salidas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Traslado Propio':
        nuevo_inventario.traslado_propio = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Traslado Remisionado':
        nuevo_inventario.traslado_remisionado = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    elif bodega.nombre == 'Ventas':
        nuevo_inventario.ventas = Item.objects.filter(
            numero_item=instance.numero_item, bodega=instance.bodega
        ).aggregate(Sum('cantidad_cajas'))['cantidad_cajas__sum'] or 0
        nuevo_inventario.save()
    else:
        # Manejo de error y envío de alerta
        logging.error(f"Condición no manejada para la bodega: {item.bodega.nombre}")
        messages.error(request, f"Condición no manejada para la bodega: {item.bodega.nombre}")
