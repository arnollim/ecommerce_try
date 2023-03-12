class Order:
    static_order_id = 0

    def __init__(self, user_id, products, grandTotal):
        Order.static_order_id += 1
        self.id = Order.static_order_id
        self.user_id = user_id
        self.products = products
        self.grandTotal = grandTotal