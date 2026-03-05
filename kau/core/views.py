from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ContactoForm
from products.models import Producto, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from .models import ConsultaContacto


def home(request):
    q = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria", "").strip()
    orden = request.GET.get("orden", "").strip()

    productos = Producto.objects.filter(activo=True).select_related("categoria")
    categorias = Categoria.objects.order_by("nombre")

    if q:
        productos = productos.filter(nombre__icontains=q)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if orden == "precio_asc":
        productos = productos.order_by("precio")
    elif orden == "precio_desc":
        productos = productos.order_by("-precio")
    elif orden == "nombre_asc":
        productos = productos.order_by("nombre")
    elif orden == "nombre_desc":
        productos = productos.order_by("-nombre")
    else:
        productos = productos.order_by("-id")

    paginator = Paginator(productos, 6)  # 6 productos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "core/home.html",
        {
            "productos": page_obj,
            "categorias": categorias,
            "q_actual": q,
            "categoria_actual": categoria_id,
            "orden_actual": orden,
        },
    )


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Gracias por escribirnos 🌿 Tu mensaje fue enviado correctamente."
            )
            return redirect("core:contacto")
    else:
        form = ContactoForm()

    return render(request, "core/contacto.html", {"form": form})


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ConsultasListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = ConsultaContacto
    template_name = "core/consultas_list.html"
    context_object_name = "consultas"
    paginate_by = 10
    ordering = ["-creado_en"]