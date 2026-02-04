from django.conf import settings
from django.db import models
from products.models import Producto


class Pedido(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pedidos",
    )
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    creado_en = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField()

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre}"


class PedidoItem(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="items",
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
    )
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.precio * self.cantidad
