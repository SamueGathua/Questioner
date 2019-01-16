from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TestSignupEndpoints(unittest.TestCase):
     def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()

     def create_record(self):
        new_rec = {
        "fname": "Sam",
        "lname": "Gat",
        "email": "Sam@abc.com",
        "password": "password"
        }
        response = self.client.post('/api/v1/user/signup',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

     def test_signup_post(self):
            r = self.create_record()
            self.assertEqual(r.status_code, 201)

     def test_user_authentication_post(self):
        self.create_record()
        response = self.client.post('/api/v1/user/login', \
            data=json.dumps({
                "email" : "Sam@abc.com",
                "password" : "password",
                }),\
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)
