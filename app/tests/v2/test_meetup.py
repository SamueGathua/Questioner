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
         response = self.client.post('/api/v2/user/login', \
            data=json.dumps({
                "email":"admin@example.com",
	            "password":"123abc&&"
                }),\
            headers={"content-type": "application/json"})

         self.get_token = response.get_json()['token']
         self.header = {"Authorization":"Bearer "+self.get_token}


     def create_record(self):
         new_rec = {
	              "title":"Buy me lunch",
	              "description":"Flask and FlaskVery Long",
	              "venue":"Heart",
	              "date":"20/Jan/2019",
	              "tags":"Technology"
                }
         response = self.client.post('/api/v2/meetups',
                            data=json.dumps(new_rec),
                            content_type="application/json",
                            headers = self.header)
         return response

     def test_meetup_post_(self):
         r = self.create_record()
         self.assertEqual(r.status_code, 201)

     def test_get_meetups(self):
         r = self.client.get("/api/v2/meetups", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)

     def test_get_specific_meetups(self):
          r = self.client.get("/api/v2/meetups/6", headers={"content-type": "application/json"})
          self.assertEqual(r.status_code, 200)

     def test_delete_meetups_unauthorized(self):
         r = self.client.delete("/api/v2/meetups/1", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 401)
