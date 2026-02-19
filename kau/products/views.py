from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Producto
from .forms import ProductoForm


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ProductoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Producto
    template_name = "products/product_list.html"
    context_object_name = "productos"
    queryset = Producto.objects.select_related("categoria")


class ProductoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente.")
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)


class ProductoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Producto
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
