from django.contrib import messages
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from .session_cart import Cart


def _safe_int(value, default=1):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


@require_POST
def cart_add(request):
    cart = Cart(request)

    product_id = request.POST.get("product_id")
    quantity = _safe_int(request.POST.get("quantity"), default=1)

    if not product_id:
        return JsonResponse({"ok": False, "error": "product_id requerido"}, status=400)

    if quantity < 1:
        quantity = 1

    cart.add(product_id=product_id, quantity=quantity)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
    })

@require_POST
def cart_update(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    try:
        quantity = int(request.POST.get("quantity", 1))
    except (TypeError, ValueError):
        quantity = 1

    if not product_id:
        messages.error(request, "No se pudo actualizar la cantidad.")
        return redirect("cart:detail")

    if quantity < 1:
        quantity = 1

    cart.update(product_id, quantity)
    messages.success(request, "Cantidad actualizada.")
    return redirect("cart:detail")

@require_POST
def cart_remove(request):
    """
    Remove para la página /cart/ (Tu Kau). POST + redirect.
    """
    cart = Cart(request)
    product_id = request.POST.get("product_id")

    if not product_id:
        messages.error(request, "No se pudo quitar el producto del carrito.")
        return redirect("cart:detail")

    cart.remove(product_id)
    messages.success(request, "Producto eliminado del carrito.")
    return redirect("cart:detail")


@require_POST
def cart_remove_ajax(request):
    """
    Remove para el side-cart (AJAX). POST + JSON.
    """
    cart = Cart(request)
    product_id = request.POST.get("product_id")

    if not product_id:
        return JsonResponse({"ok": False, "error": "product_id requerido"}, status=400)

    cart.remove(product_id)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
        "total_price": str(cart.get_total_price()),
    })


@require_POST
def cart_update_ajax(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    quantity = _safe_int(request.POST.get("quantity"), default=1)

    if not product_id:
        return JsonResponse({"ok": False, "error": "product_id requerido"}, status=400)

    if quantity < 1:
        quantity = 1

    cart.update(product_id, quantity)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
        "total_price": str(cart.get_total_price()),
    })


def side_cart(request):
    cart = Cart(request)

    html = render_to_string(
        "cart/side_cart.html",
        {"cart": cart},
        request=request
    )

    return JsonResponse({
        "html": html,
        "total_items": cart.total_items,
    })


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})


def cart_clear(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    cart = Cart(request)
    cart.clear()
    messages.warning(request, "Carrito vaciado.")
    return redirect("cart:detail")