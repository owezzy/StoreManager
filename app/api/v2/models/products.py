import psycopg2
from app.db import cur


class ProductsModel:
    def __init__(self, product_name, price, stock, minimum_stock, owner):
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.minimum_stock = minimum_stock
        self.owner = owner

    # adds a product to a list of products
    def add_product(self):
        try:
            cur.execute(
                """insert into products(product_name, price, stock,minimum_stock, owner)
                values (%s, %s, %s, %s, %s, %s)""",
                (self.product_name, self.price, self.stock, self.minimum_stock, self.owner))
            cur.commit()
            return 'product created successfully'
        except (Exception, psycopg2.Error) as er:
            return {'message': 'Something went wrong',
                    'error': er}, 500

    @staticmethod
    def get_all_product():
        try:
            cur.execute("""SELECT * FROM products """)
            rows = cur.fetchall()
            return rows
        except (Exception, psycopg2.Error) as er:
            return {'message': 'Something went wrong',
                    'error': er}, 500

    @staticmethod
    def get_product(product_id):
        # fetch a single product
        try:
            cur.execute("""SELECT * FROM products WHERE id='{}' """.format(product_id))
            rows = cur.fetchall()
            if not rows:
                return False
            return rows

        except (Exception, psycopg2.Error) as e:
            return {'message': 'Something went wrong',
                    'error': e}, 500

    @staticmethod
    def find_by_id(product_id):
        cur.execute("""SELECT * FROM products WHERE id='{}' """.format(product_id))
        rows = cur.fetchone()
        if rows:
            return True
        return False

    @staticmethod
    def check_product_name(product_name):
        cur.execute("""SELECT * FROM products WHERE product_name='{}' """.format(product_name))
        rows = cur.fetchone()
        return rows
