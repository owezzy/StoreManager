import unittest
import json
import sys
from psycopg2 import connect, extras
from app.app import create_app
from app.db import create_tables, delete_table


REGISTRATION_URL = '/api/v2/registration/'
LOGIN_URL = '/api/v2/login/'


class UserRegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.register_new_user = {"email": "owen@gmail.com", "password": "qwerty@123", "username": "kunta",
                                  "user_id": 1}
        self.register_user_empty_email = {"email": "", "password": "abc@123", "username": "test"}
        self.register_user_invalid_email = {"email": "owen#gmailcom", "password": "abc@123", "username": "test"}
        self.register_user_empty_username = {"email": "owen@gmail.com", "password": "abc@123", "username": ""}
        self.register_user_empty_password = {"email": "owen@gmail.com", "password": "", "username": "test"}
        self.login_user = {"email": "owenobezzy@gmail.com", "password": "abc@123"}
        self.login_user_empty_email = {"email": "", "password": "abc@123"}
        self.login_user_empty_password = {"email": "owenobezzy@gmail.com", "password": ""}

        create_tables()

    def test_post(self):
        res = self.client.post(REGISTRATION_URL, data=json.dumps(self.register_new_user),
                               content_type = 'application/json')
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['message'], 'User created successfully.')

    def test_post_user_empty_email(self):
        res = self.client.post(REGISTRATION_URL, data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(resp_data['message'], 'Email is required', 400)

    def test_post_user_invalid_email(self):
        res = self.client.post(REGISTRATION_URL, data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_post_user_empty_username(self):
        res = self.client.post(REGISTRATION_URL, data=json.dumps(self.register_user_empty_username),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_post_user_empty_password(self):
        res = self.client.post(REGISTRATION_URL, data=json.dumps(self.register_user_empty_password),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

