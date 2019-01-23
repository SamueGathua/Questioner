from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.meetup_models import MeetupRecords
from ..models.base_models import User

class Meetup(Resource, MeetupRecords):
    def __init__(self):

        self.records = MeetupRecords()
        self.parser = reqparse.RequestParser()
        self.check_admin = User()
        #validates the key and data types  for the meetup record

        self.parser.add_argument('title', type=str, required=True, help='Invalid key for title')
        self.parser.add_argument('description', type=str, required=True, help='Invalid key for description')
        self.parser.add_argument('venue', type=str, required=True, help='Invalid key for venue')
        self.parser.add_argument('date', type=str, required=True, help='Invalid key for date')
        self.parser.add_argument('tags', type=str, required=True, help='Invalid key in tags')

    def get(self):
        return make_response(jsonify({"status":200,
                                    "The available meetup records are": self.records.get_all_meetup_records()}), 200)

    @jwt_required
    def post(self):
        reqdata = self.parser.parse_args(strict=True)
        author = get_jwt_identity()
        """validates that the data received is not null"""
        """"if the null an error message is thrown"""
        if not self.check_admin.check_is_admin(author):
            return make_response(jsonify({"status":401,
                                       "message":" This service is for admin only"}), 401)
        if not reqdata['title'] or not reqdata['title'].strip():
            return make_response(jsonify({"status":400,
                                       "error":" The title field is required"}), 400)
        if not reqdata['description'] or  not reqdata['description'].strip():
            return make_response(jsonify({"status":400,
                                       "error":"The description field is required"}), 400)
        if not reqdata['venue'] or not reqdata['venue'].strip() :
            return make_response(jsonify({"status":400,
                                       "error":"The venue field is required"}), 400)
        if not reqdata['date']:
            return make_response(jsonify({"status":400,
                                       "error":"The date field is required"}), 400)
        if not reqdata['tags']:
            return make_response(jsonify({"status":400,
                                       "error":"The Tags field is required"}), 400)

        else:
            """Executed when all the above validations pass"""

            res = self.records.save(reqdata,author)

            return make_response(jsonify({"status":201,
                                         "message":"A new record with the following data has been added",
                                         "data": res}), 201)

                                         
class MeetupId(Resource, MeetupRecords):
    def __init__(self):
        self.records = MeetupRecords()

    def get(self, id):
        if self.records.get_specific_meetup_record(id):
            rec =self.records.get_specific_meetup_record(id)
            return make_response(jsonify({"status":200,
                                        "The requested meetup record has the following details": rec}), 200)
        else:
            """if the requested data does not exist"""
            return make_response(jsonify({"status":200,
                                        "Error": "Meetup record not found"}), 404)
