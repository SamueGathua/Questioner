from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.question_models import QuestionRecords


class Question(QuestionRecords, Resource):
    def __init__(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('question', type=str, required=True, help='Invalid  key for question')
        self.records = QuestionRecords()

    @jwt_required
    def post(self, id):
        author = get_jwt_identity()
        data = self.parser.parse_args(strict=True)
        #Checks that data received from post question is not empty
        if not data['question']:
            #if data received is empty an error message is thrown
            return make_response(jsonify({"status":400,
                                       "Error":"Qestion field cannot be empty"}), 400)
        question = data['question']
        responce = self.records.save(id, question, author)
        return make_response(jsonify({"status":201,
                                    "A new question record has been created with the following details": responce}), 201)
