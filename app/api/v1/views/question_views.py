from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from ..models.question_models import QuestionRecords, VotingRecord

class Question(QuestionRecords, Resource):
    def __init__(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('question', type=str, required=True, help='Invalid key')
        reqdata = self.parser.parse_args(strict=True)
        self.records = QuestionRecords()

    def post(self, id):
        reqdata = self.parser.parse_args(strict=True)
        data = request.get_json()

        #Checks that data received from post question is not empty

        if not reqdata['question']:
            #if data received is empty an error message is thrown

            return make_response(jsonify({"status":400,
                                       "Error":"Qeestion field cannot be empty"}), 400)

        #Executed wgen  all above checks pass
        responce = self.records.save(id, reqdata['question'])
        return make_response(jsonify({"status":201,
                                    "A new question record has been created with the following details": responce}), 201)
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
