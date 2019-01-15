from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from ..models.meetup_models import MeetupRecords, ConfirmRecords

class Meetup(Resource, MeetupRecords):
    def __init__(self):

        self.records = MeetupRecords()
        self.parser = reqparse.RequestParser()

        #validates the key and data types  for the meetup record

        self.parser.add_argument('title', type=str, required=True, help='Invalid key')
        self.parser.add_argument('description', type=str, required=True, help='Invalid key')
        self.parser.add_argument('venue', type=str, required=True, help='Invalid key')
        self.parser.add_argument('date', type=str, required=True, help='Invalid key')


    def post(self):

        reqdata = self.parser.parse_args(strict=True)
        data = request.get_json()

        #validates that the data received is not null
        #if the null an error message is thrown
        if not reqdata['title']:
            return make_response(jsonify({"status":400,
                                       "Error":" The title field is required"}), 400)
        if not reqdata['description']:
            return make_response(jsonify({"status":400,
                                       "Error":"The description field is required"}), 400)
        if not reqdata['venue']:
            return make_response(jsonify({"status":400,
                                       "Error":"The venue field is required"}), 400)
        if not reqdata['date']:
            return make_response(jsonify({"status":400,
                                       "Error":"The date field is required"}), 400)

        else:
            #Executed when all the above validations password

            res = self.records.save(reqdata['title'], reqdata['description'],  reqdata['venue'],reqdata['date'])

            return make_response(jsonify({"status":201,
                                       "A new record with the following data has been added": res}), 201)


    def get(self):
        res = self.records.get_records()
        return make_response(jsonify({"status":200,
                                    "The available records are": res}), 200)

class MeetupId(Resource, MeetupRecords):
    def __init__(self):
        self.records = MeetupRecords()

    def get(self, id):
        rec = self.records.find(id)
        if rec:
            return make_response(jsonify({"status":200,
                                        "The requested record has the following details": rec}), 200)
        else:
            #if the requested data does not exist

            return make_response(jsonify({"status":200,
                                        "Error": "Meetup record not found"}), 404)

class ConfirmAttendance(ConfirmRecords, Resource):
    def __init__(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('confirm', type=str, required=True, help='Invalid key')

        self.records = ConfirmRecords()


    def get(self, m_id):
        rec = self.records.get_confirms(m_id)
        if rec:
            return make_response(jsonify({"status":200,
                                        "The selected meetup has the following confirmations": rec}), 200)


    def post(self, m_id):
        reqdata = self.parser.parse_args(strict=True)
        data = request.get_json()
        #checks that the data received is not null

        if not reqdata['confirm']:
            return make_response(jsonify({"status":400,
                                        "Error":"The field cannot be empty"}), 400)


        else:
            responce = self.records.save(m_id, reqdata['confirm'])
            return make_response(jsonify({"status":201,
                                        "A new confirm Attendance record has been created with the following details": responce}), 201)
