from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from cart.session_cart import Cart
from .forms import CheckoutForm
from .models import Pedido, PedidoItem


@login_required
def checkout(request):
    cart = Cart(request)

    # Validar carrito vacío
    if cart.total_items == 0:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect("cart:detail")

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # Crear pedido asociado al usuario logueado
            pedido = Pedido.objects.create(
                usuario=request.user,
                nombre=form.cleaned_data["nombre"],
                email=form.cleaned_data["email"],
                total=cart.get_total_price(),
            )

            # Crear items del pedido
            for item in cart:
                PedidoItem.objects.create(
                    pedido=pedido,
                    producto=item["producto"],
                    precio=item["price"],
                    cantidad=item["quantity"],
                )

            # Vaciar carrito
            cart.clear()

            return redirect("orders:success", order_id=pedido.id)

    else:
        form = CheckoutForm()

    return render(request, "orders/checkout.html", {
        "form": form,
        "cart": cart
    })


@login_required
def success(request, order_id):
    pedido = get_object_or_404(Pedido, id=order_id, usuario=request.user)

    return render(request, "orders/success.html", {
        "pedido": pedido
    })


@login_required
def mis_pedidos(request):
    pedidos = (
        Pedido.objects
        .filter(usuario=request.user)
        .prefetch_related("items__producto")
        .order_by("-creado_en")
    )

    return render(request, "orders/mis_pedidos.html", {
        "pedidos": pedidos
    })