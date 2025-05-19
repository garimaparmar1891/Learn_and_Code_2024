class cartDTO:
    def __init__(self, product, quantity, price, added_at):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.added_at = added_at

    def to_dict(self):
        return {
            "product": self.product,
            "quantity": self.quantity,
            "price": self.price,
            "added_at": self.added_at
        }
