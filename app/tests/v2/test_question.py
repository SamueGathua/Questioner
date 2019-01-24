from app import create_app
from run import app
from flask.testing import FlaskClient
import unittest
import json

class TestQuestions(unittest.TestCase):
    def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()
    def create_record(self):
        new_rec = {
        "question": "Who discovered python?"
        }
        response = self.client.post('/api/v2/meetups/1/questions',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_question_post_anauthorized(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 401)
