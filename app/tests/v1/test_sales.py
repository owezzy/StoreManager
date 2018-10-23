import unittest
import json
from app import create_app


ADD_PRODUCT = '/api/v1/products'


class TestEntryCase(unittest.TestCase):
    def setUp(self):
        '''initialize api and set test variables'''
        self.app = create_app('testing')