from django.contrib import admin
from .models import Pedido, PedidoItem


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email", "total", "estado", "creado_en")
    list_filter = ("estado", "creado_en")
    search_fields = ("id", "nombre", "email", "usuario__username")
    inlines = [PedidoItemInline]


@admin.register(PedidoItem)
class PedidoItemAdmin(admin.ModelAdmin):
    list_display = ("id", "pedido", "producto", "precio", "cantidad")
    search_fields = ("pedido__id", "producto__nombre")