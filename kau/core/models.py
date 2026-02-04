from django.db import models


class ConsultaContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Consulta de contacto"
        verbose_name_plural = "Consultas de contacto"

    def __str__(self):
        return f"{self.nombre} <{self.email}>"
