from werkzeug.security import check_password_hash, generate_password_hash

products = []
orders = []
users = []


class ProductsModel:
    def __init__(self, product_name, price, stock):
        # We will automatically generate the new id
        self.id = len(products) + 1
        self.product_name = product_name
        self.price = price
        self.stock = stock

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

    @staticmethod
    def delete_product(product_id):
        return products.pop(product_id)

    @staticmethod
    def check_product_name(product_name):
        return next((item for item in products if item["product"] == product_name), False)


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
        return next((item for item in products if item["id"] == order_id), False)


class User:

    @staticmethod
    def create_new_user(username, email, password):
        role = 'user'
        user_id = len(users) + 1
        new_user = {'id': user_id, 'username': username, 'email': email, 'password': password, 'role': role}
        users.append(new_user)

    @staticmethod
    def find_by_username(username):
        return next((user for user in users if user["username"] == username), False)

    @staticmethod
    def find_by_email_address(email):
        return next((user for user in users if user["email"] == email), False)

    @staticmethod
    def generate_password_hash(raw_password):
        return generate_password_hash(raw_password)

    @staticmethod
    def verify_hash(password, email):
        user = next((u for u in users if u["email"] == email), False)
        if user == False: # try if not user later
            return False
        return check_password_hash(password, user['password'])
