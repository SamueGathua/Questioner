from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TesstMeetupEndpoints(unittest.TestCase):
     def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()

     def create_record(self):
        new_rec = {
        "title": "Hackers hub",
        "description": "A meeting for hackers",
        "host": "Dr Hangir",
        "venue": "Mombasa",
        "date": "27th of December"
        }
        response = self.client.post('/api/v1/meetups',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

     def test_post(self):
         r = self.create_record()
         self.assertEqual(r.status_code, 201)
     def test_get(self):
         self.create_record()
         r = self.client.get("/api/v1/meetups", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)
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
