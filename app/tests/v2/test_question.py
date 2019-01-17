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
        response = self.client.post('/api/v2/meetups/4/questions',
                            data=json.dumps(new_rec),
                            headers={"content-type": "application/json"})
        return response

    def test_question_post(self):
        r = self.create_record()
        self.assertEqual(r.status_code, 201)


class TestVoting(unittest.TestCase):
    def setUp(self):
         app.testing = True
         self.app = create_app()
         self.client = self.app.test_client()

    def test_upvote_patch(self):
        response = self.client.patch('/api/v2/questions/1/upvotes',
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)

    def test_downvote_patch(self):
        response = self.client.patch('/api/v2/questions/1/downvotes',
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)
