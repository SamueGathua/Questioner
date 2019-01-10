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
        "uname": "Sam",
        "email": "Sam@abc.com",
        "password": "password"

        }
        response = self.client.post('/api/v1/meetups',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response
