import unittest
import json

from app.app import create_app

POST_ORDER = '/api/v2/sales'
GET_A_SINGLE_ORDER = '/api/v2/sales/1'
GET_ALL_ORDER = '/api/v2/sales'


class TestOrder(unittest.TestCase):
    def setUp(self):
        """initialize api and set test variables"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.create_order = json.dumps(dict(
            product_name="shoes",
            customer_name="kunta",
            attendant_name="Kinte",
            cost=4000,
            quantity=1

        ))

    def test_get_orders(self):
        """test we can get orders"""
        resource = self.client.get(POST_ORDER,
                                   data=json.dumps(self.create_order),
                                   content_type='application/json')
        get_data = json.dumps(resource.data.decode())
        print(get_data)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(resource.status_code, 200)

    def test_post_orders(self):
        """Test for post product"""
        resource = self.client.post(
            POST_ORDER,
            data=self.create_order,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201, msg='CREATED')
        self.assertEqual(resource.content_type, 'application/json')


class TestGetSingleOrder(unittest.TestCase):
    def test_get(self):
        self.fail()


class TestPostOrder(unittest.TestCase):
    def test_post(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
