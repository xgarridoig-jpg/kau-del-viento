from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactoForm
from products.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from .models import ConsultaContacto


def home(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, "core/home.html", {"productos": productos})


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