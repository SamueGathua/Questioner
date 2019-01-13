from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.question_models import Records
from ....utils.validators import Validations


class Question(Records, Resource):
    def __init__(self):
        self.validate = Validations()
        self.records = Records()

    def post(self, id):
        data = request.get_json()
        data_valid = self.validate.validate_question_keys(data)
        if data_valid:
            meetup_id = id
            question = data['question']
            responce = self.records.save(meetup_id, question)
            return make_response(jsonify({"A new question record has been created with the following details": responce}), 201)
        else:
             return make_response(jsonify({"Error":"Unrecognised field"}), 400)


class Voting(Records, Resource):
    def __init__(self):
        self.records = Records()

    def post(self, q_id):
        data = request.get_json()
        question_id = q_id
        vote = data['vote']
        responce = self.records.save(question_id, vote)
        return make_response(jsonify({"A new vote record has been created with the following details": responce}), 201)
