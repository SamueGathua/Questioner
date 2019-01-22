from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TestSignupDatabase(unittest.TestCase):
     def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()

     def create_record(self):
        new_rec = {
            "firstname":"Sam",
	        "lastname":"Akote",
	        "othername":"sothee",
	        "phonenumber":"0707089765",
	        "email":"sam@example.com",
	        "password":"SamAkot12&",
	        "isadmin":"True"
        }
        response = self.client.post('/api/v2/user/signup',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

     def test_signup_post(self):
            resp = self.create_record()
            self.assertEqual(resp.status_code, 201)
