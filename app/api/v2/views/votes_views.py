from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.votes_models import VotesRecords


class Votes(Resource, VotesRecords):
    def __init__(self):
        self.records = VotesRecords()

    @jwt_required
    def patch(self, q_id):

        data = request.get_json()
        vote = data['vote']
        #checks that the data received is not null

        if not vote.strip():
            return make_response(jsonify({"status":400,
                                        "error":"The field cannot be empty"}), 400)
        if vote.strip():
            if vote == "up":
                responce = self.records.save_upvote(q_id, vote)
                return make_response(jsonify({"status":201,
                                        "message":"You have upvoted the question"}), 201)
            if vote == "down":
                responce = self.records.save_downvote(q_id, vote)
                return make_response(jsonify({"status":201,
                                        "message":"You have upvoted the question" }), 201)

            return make_response(jsonify({"status":400,
                                    "error":"Accepted forms are 'up' and 'down'"}), 400)
