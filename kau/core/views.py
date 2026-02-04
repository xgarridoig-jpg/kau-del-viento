from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactoForm


def home(request):
    return render(request, "core/home.html")


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gracias por contactarnos. Te responderemos pronto.")
            return redirect("core:contacto")
    else:
        form = ContactoForm()

    return render(request, "core/contacto.html", {"form": form})
