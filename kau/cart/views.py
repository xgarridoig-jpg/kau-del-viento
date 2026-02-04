from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .session_cart import Cart


@require_POST
def cart_add(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity", 1))
    cart.add(product_id=product_id, quantity=quantity)
    messages.success(request, "Producto agregado al carrito.")
    return redirect("cart:detail")


@require_POST
def cart_remove(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    cart.remove(product_id)
    messages.info(request, "Producto eliminado del carrito.")
    return redirect("cart:detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.warning(request, "Carrito vaciado.")
    return redirect("cart:detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
