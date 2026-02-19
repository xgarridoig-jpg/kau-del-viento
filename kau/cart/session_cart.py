from decimal import Decimal
from products.models import Producto


class Cart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)

        if not cart:
            cart = self.session[self.SESSION_KEY] = {}

        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        producto = Producto.objects.get(id=product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(producto.precio),
            }

        self.cart[product_id]["quantity"] += int(quantity)
        self.save()

    def update(self, product_id, quantity):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]["quantity"] = int(quantity)
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

    def __iter__(self):
        product_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=product_ids)

        for producto in productos:
            item = self.cart[str(producto.id)]
            price = Decimal(item["price"])
            quantity = item["quantity"]

            yield {
                "producto": producto,
                "quantity": quantity,
                "price": price,
                "total_price": price * quantity,
            }

    @property
    def total_items(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )
