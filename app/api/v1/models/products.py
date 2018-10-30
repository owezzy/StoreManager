products = []


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
