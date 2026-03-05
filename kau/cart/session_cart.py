from decimal import Decimal
from products.models import Producto


class Cart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if cart is None:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, product_id, quantity=1, override_quantity=False):
        product_id = str(product_id)

        if quantity < 1:
            quantity = 1

        if product_id not in self.cart:
            producto = Producto.objects.get(id=product_id)
            # guardamos precio como string para evitar problemas de JSON/Decimal
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(producto.precio),
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def update(self, product_id, quantity):
        product_id = str(product_id)

        if product_id not in self.cart:
            return

        if quantity < 1:
            quantity = 1

        self.cart[product_id]["quantity"] = quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session[self.SESSION_KEY] = {}
        self.save()

    def save(self):
        self.session.modified = True

    @property
    def total_items(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            (Decimal(item["price"]) * item["quantity"])
            for item in self.cart.values()
        )

    def __iter__(self):
        product_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=product_ids)

        productos_map = {str(p.id): p for p in productos}

        for product_id, item in self.cart.items():
            producto = productos_map.get(str(product_id))
            if not producto:
                continue

            price = Decimal(item["price"])
            quantity = int(item["quantity"])
            yield {
                "producto": producto,
                "price": price,
                "quantity": quantity,
                "total_price": price * quantity,
            }