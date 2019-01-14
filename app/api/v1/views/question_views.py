from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.question_models import QuestionRecords, VotingRecord
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

class Upvotes(VotingRecord, Resource):
    def __init__(self):
        self.rec = VotingRecord()

    def patch(self, id):
        response = self.rec.vote(id, True)
        return make_response(jsonify({"status":201,
                                    "The voting record has been updated with the following details": response}), 201)


class Downvotes(VotingRecord, Resource):
    def __init__(self):
        self.rec = VotingRecord()

    def patch(self, id):
        response = self.rec.vote(id, False)
        return make_response(jsonify({"status":201,
                                    "The voting record has been updated with the following details": response}), 201)
