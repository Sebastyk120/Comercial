from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from comercial.models import Presentacion


class Cotizacion(models.Model):
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    semana = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(56)], verbose_name="Semana")
    precio_fob = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comision_fob = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_dxb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comision_dxb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.presentacion} - semana: {self.semana}"
