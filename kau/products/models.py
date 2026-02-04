from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ("flora", "Flora seca"),
        ("madera", "Madera"),
        ("textil", "Textil"),
        ("vivero", "Vivero"),
    ]

    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="productos/")
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
