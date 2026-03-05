from django.conf import settings
from django.db import models
from products.models import Producto


class Pedido(models.Model):
    ESTADO_PENDIENTE = "pendiente"
    ESTADO_CONFIRMADO = "confirmado"
    ESTADO_ENVIADO = "enviado"
    ESTADO_ENTREGADO = "entregado"
    ESTADO_CANCELADO = "cancelado"

    ESTADOS_CHOICES = [
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_CONFIRMADO, "Confirmado"),
        (ESTADO_ENVIADO, "Enviado"),
        (ESTADO_ENTREGADO, "Entregado"),
        (ESTADO_CANCELADO, "Cancelado"),
    ]

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
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_CHOICES,
        default=ESTADO_PENDIENTE,
    )

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

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"