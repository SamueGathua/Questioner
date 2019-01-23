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

     def test_get_meetups(self):
         r = self.client.get("/api/v1/meetups", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)
         r = self.client.get("/api/v1/meetups/1", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)
    
