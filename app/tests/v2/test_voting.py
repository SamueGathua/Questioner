from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TestVoting(unittest.TestCase):
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
         "vote": "up"
         }
         response = self.client.patch('/api/v2/questions/1/votes',
                            data=json.dumps(new_rec),
                            content_type="application/json",
                            headers = self.header)
         return response

    def test_vote_patch(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)
