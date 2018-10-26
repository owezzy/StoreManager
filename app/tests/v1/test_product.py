import unittest
import json
import sys

from app.app import create_app

POST_PRODUCT_URL = '/api/v1/products'
GET_A_SINGLE_PRODUCT = '/api/v1/product/1'
GET_ALL_PRODUCTS = '/api/v1/products'


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Initialize the api with test variable"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.create_product = json.dumps(dict(
            product_name="shoes",
            stock=2,
            price=3000
        ))
        self.missing_product_name = json.dumps(dict(
            product_name="",
            stock=2,
            price=3000
        ))

    def test_add_product(self):
        """Test for post product"""
        resource = self.client.post(
            POST_PRODUCT_URL,
            data=self.create_product,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201, msg='CREATED')
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_products(self):
        """test we can get products"""
        resource = self.client.get(POST_PRODUCT_URL,
                                   data=json.dumps(self.create_product),
                                   content_type='application/json')
        get_data = json.dumps(resource.data.decode())
        print(get_data)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(resource.status_code, 200)

    def test_get(self):
        """test we can get a single products"""
        resource = self.client.get(GET_A_SINGLE_PRODUCT)
        self.assertEqual(resource.status_code, 404)


if __name__ == '__main__':
    unittest.main()
