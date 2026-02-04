from django.contrib import messages
from django.shortcuts import redirect, render
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
            messages.success(request, "Pedido creado correctamente.")
            return redirect("orders:success", pedido_id=pedido.id)
    else:
        form = CheckoutForm()

    return render(request, "orders/checkout.html", {"form": form, "cart": cart})


def success(request, pedido_id):
    return render(request, "orders/success.html", {"pedido_id": pedido_id})
