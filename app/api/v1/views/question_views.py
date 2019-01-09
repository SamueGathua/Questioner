from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.question_models import QuestionRecord
class Question(QuestionRecord, Resource):
    def __init__(self):
        self.records = QuestionRecord()

    def post(self, id):
        data = request.get_json()
        meetup_id = id
        question = data['question']
        responce = self.records.save(meetup_id, question)
        return make_response(jsonify({"A new question record has been created with the following details": responce}), 201)
