from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TestConfirm(unittest.TestCase):
    def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()
    def create_record(self):
        new_rec = {
        "confirm": "Yes?"
        }
        response = self.client.post('/api/v1/meetups/4/confirms',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_confirm_post(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)
