from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.voting_models import VotingRecord
class Voting(VotingRecord, Resource):
    def __init__(self):
        self.records = VotingRecord()

    def post(self, id):
        data = request.get_json()
        question_id = id
        vote = data['vote']
        responce = self.records.save(question_id, vote)
        return make_response(jsonify({"A new vote record has been created with the following details": responce}), 201)
