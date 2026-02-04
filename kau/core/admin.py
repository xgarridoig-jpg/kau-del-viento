from django.contrib import admin
from .models import ConsultaContacto


@admin.register(ConsultaContacto)
class ConsultaContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "creado_en")
    search_fields = ("nombre", "email")
    list_filter = ("creado_en",)
