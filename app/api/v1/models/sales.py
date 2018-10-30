orders = []


class SalesModel:
    def __init__(self, product_name, attendant_name, customer_name, cost, quantity):
        # We will automatically generate the new oder_id
        self.id = len(orders) + 1
        self.product_name = product_name
        self.attendant_name = attendant_name
        self.customer_name = customer_name
        self.quantity = quantity
        self.cost = cost

    # adds a product to a list of products
    def add_order(self):
        new_order = {'id': self.id, 'product_name': self.product_name, 'attendant_name': self.attendant_name,
                     'cost': self.cost, 'customer_name': self.customer_name}
        orders.append(new_order)
        return new_order

    @staticmethod
    def get_all_orders():
        return orders

    @staticmethod
    def get_order(order_id):
        return next((item for item in orders if item["id"] == order_id), False)


