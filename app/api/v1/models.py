products = []


class ProductsModel:
    def __init__(self, product_name, price, stock, creation_date):
        # We will automatically generate the new id
        self.id = len(products) + 1
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.creation_date = creation_date

    # adds a product to a list of products
    def add_product(self):
        new_product = {'id': self.id, 'product': self.product_name, 'price': self.price, 'stock': self.stock}
        products.append(new_product)
        return new_product

    @staticmethod
    def get_all_product():
        return products

    @staticmethod
    def get_product(product_id):
        return next((item for item in products if item["id"] == product_id), False)

    def delete_product(product_id):
        pass

    @staticmethod
    def check_product_name(product_name):
        return next((item for item in products if item["product"] == product_name), False)


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
