from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.question_models import QuestionRecords, VotingRecords
from ....utils.validators import Validations


class Question(QuestionRecords, Resource):
    def __init__(self):
        self.validate = Validations()
        self.records = QuestionRecords()

    def post(self, id):
        data = request.get_json()
        data_valid = self.validate.validate_question_keys(data)
        #validate the key data for the question record
        if data_valid:
            meetup_id = id
            question = data['question']
            responce = self.records.save(meetup_id, question)
            return make_response(jsonify({"status":201,
                                        "A new question record has been created with the following details": responce}), 201)
        else:
            #when an invalid key is parsed
             return make_response(jsonify({"status":400,
                                        "Error":"Unrecognised key"}), 400)


class Voting(VotingRecords, Resource):
    def __init__(self):
        self.records = VotingRecords()

    def post(self, q_id):
        data = request.get_json()
        question_id = q_id
        vote = data['vote']
        responce = self.records.save(question_id, vote)
        return make_response(jsonify({"status":201,
                                    "A new vote record has been created with the following details": responce}), 201)
