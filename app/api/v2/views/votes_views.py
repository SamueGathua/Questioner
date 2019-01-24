from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.votes_models import VotesRecords

class Votes(Resource, VotesRecords):
    def __init__(self):
        self.records = VotesRecords()
        self.parser = reqparse.RequestParser()
        """validates the key and data types  for the voting record"""
        self.parser.add_argument('vote', type=str, required=True, help='Invalid key for Vote')

    @jwt_required
    def patch(self, q_id):

        data = self.parser.parse_args(strict=True)
        vote = data['vote']
        """checks that the data received is not null"""
        if not vote.strip():
            return make_response(jsonify({"status":400,
                                        "error":"The field cannot be empty"}), 400)
        if vote.strip():
            if vote == "up":
                responce = self.records.save_upvote(q_id, data)
                return make_response(jsonify({"status":201,
                                        "message":"You have upvoted the question"}), 201)
            if vote == "down":
                responce = self.records.save_downvote(q_id, data)
                return make_response(jsonify({"status":201,
                                        "message":"You have downvoted the question" }), 201)

            return make_response(jsonify({"status":400,
                                    "error":"Accepted formats are 'up' and 'down'"}), 400)
