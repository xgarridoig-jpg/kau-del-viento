from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactoForm
from products.models import Producto


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
