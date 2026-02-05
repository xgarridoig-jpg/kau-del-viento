from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from cart.session_cart import Cart

from .forms import CheckoutForm
from .models import Pedido, PedidoItem


def checkout(request):
    cart = Cart(request)

    if cart.total_items() == 0:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect("cart:detail")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            pedido = Pedido.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                nombre=form.cleaned_data["nombre"],
                email=form.cleaned_data["email"],
                total=cart.total_price(),
            )

            for item in cart:
                PedidoItem.objects.create(
                    pedido=pedido,
                    producto=item["producto"],
                    precio=item["producto"].precio,
                    cantidad=item["quantity"],
                )

            cart.clear()
            return redirect("orders:success", order_id=pedido.id)

    else:
        form = CheckoutForm()

    return render(request, "orders/checkout.html", {
        "form": form,
        "cart": cart
    })


def success(request, order_id):
    pedido = get_object_or_404(Pedido, id=order_id)
    return render(request, "orders/success.html", {
        "pedido": pedido
    })
