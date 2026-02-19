from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.http import JsonResponse
from .session_cart import Cart


@require_POST
def cart_add(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity", 1))

    cart.add(product_id=product_id, quantity=quantity)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
    })


@require_POST
def cart_remove(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")

    cart.remove(product_id)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
        "total_price": cart.get_total_price(),
    })


@require_POST
def cart_update_ajax(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity", 1))

    cart.update(product_id, quantity)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
        "total_price": cart.get_total_price(),
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
    cart = Cart(request)
    cart.clear()

    messages.warning(request, "Carrito vaciado.")
    return redirect("cart:detail")

@require_POST
def cart_remove_ajax(request):
    cart = Cart(request)
    product_id = request.POST.get("product_id")

    cart.remove(product_id)

    return JsonResponse({
        "ok": True,
        "total_items": cart.total_items,
        "total_price": cart.get_total_price(),
    })