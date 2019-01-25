from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json


class TestUser(unittest.TestCase):
    def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()

    def test_user_login_wrong_password(self):

        response = self.client.post('/api/v2/user/login', \
            data=json.dumps({
                "email":"admin@example.com",
	            "password":"12&&"
                }),\
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 400)

    def create_user_record(self):
        new_rec = {
        "firstname":"Samuel2",
        "lastname":"Gathuae",
        "othername":"userother",
        "phonenumber":"0745789012",
        "email":"gathua@example.com",
        "password":"1c&&"

        }
        response = self.client.post('/api/v2/user/signup',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_post_with_invalid_password(self):
         r = self.create_user_record()
         self.assertEqual(r.status_code, 400)
