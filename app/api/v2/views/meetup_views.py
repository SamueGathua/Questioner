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

        self.parser.add_argument('title', type=str, required=True, help='Invalid key')
        self.parser.add_argument('description', type=str, required=True, help='Invalid key')
        self.parser.add_argument('venue', type=str, required=True, help='Invalid key')
        self.parser.add_argument('date', type=str, required=True, help='Invalid key')
        self.parser.add_argument('tags', type=str, required=True, help='Invalid key')


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
                                       "Error":" The title field is required"}), 400)
        if not reqdata['description'] or  not reqdata['description'].strip():
            return make_response(jsonify({"status":400,
                                       "Error":"The description field is required"}), 400)
        if not reqdata['venue'] or not reqdata['venue'].strip() :
            return make_response(jsonify({"status":400,
                                       "Error":"The venue field is required"}), 400)
        if not reqdata['date']:
            return make_response(jsonify({"status":400,
                                       "Error":"The date field is required"}), 400)
        if not reqdata['tags']:
            return make_response(jsonify({"status":400,
                                       "Error":"The Tags field is required"}), 400)

        else:
            """Executed when all the above validations pass"""

            res = self.records.save(reqdata,author)

            return make_response(jsonify({"status":201,
                                         "message":"A new record with the following data has been added",
                                         "data": res}), 201)
