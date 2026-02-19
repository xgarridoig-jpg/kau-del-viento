from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "categoria",
        "precio",
        "activo",
        "creado_en",
    )

    list_filter = (
        "categoria",
        "activo",
        "creado_en",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )

    list_editable = ("activo",)

    ordering = ("nombre",)

    readonly_fields = ("creado_en",)
