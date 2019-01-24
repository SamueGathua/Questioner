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

    def test_vote_patch(self):
        response = self.client.patch('/api/v2/questions/1/votes',
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 401)
