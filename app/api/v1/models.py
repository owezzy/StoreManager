class ProductsModel:
    def __init__(self, product_name, price, stock, creation_date):
        # We will automatically generate the new id
        self.id = 0
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.creation_date = creation_date


class SalesModel:
    def __init__(self, product_name, attendant_name, customer_name, cost, quantity, creation_date):
        # We will automatically generate the new oder_id
        self.id = 0
        self.product_name = product_name
        self.creation_date = creation_date
        self.attendant_name = attendant_name
        self.customer_name = customer_name
        self.quantity = quantity
        self.cost = cost


class UsersModel:
    def __init__(self, email, password):
        # We will automatically generate the new id
        self.id = 0
        self.email = email
        self.password = password
