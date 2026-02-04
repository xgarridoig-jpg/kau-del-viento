class Cart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if cart is None:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = 0
        self.cart[product_id] += int(quantity)
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
        for product_id, quantity in self.cart.items():
            yield {
                "product_id": product_id,
                "quantity": quantity,
            }

    def total_items(self):
        return sum(self.cart.values())
