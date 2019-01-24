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
	      "title":"Take me out",
	      "description":"Flask and FlaskVery Long",
	      "venue":"Heart",
	      "date":"20/Jan/2019",
	      "tags":"Technology"

        }
        response = self.client.post('/api/v2/meetups',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

     def test_get_meetups(self):
         r = self.client.get("/api/v2/meetups", headers={"content-type": "application/json"})
         self.assertEqual(r.status_code, 200)

     def test_post_unauthorized(self):
         result = self.create_record()
         self.assertEqual(result.status_code, 401)

     def test_delete_meetups(self):
        r = self.client.delete("/api/v2/meetups/1", headers={"content-type": "application/json"})
        self.assertEqual(r.status_code, 401)
