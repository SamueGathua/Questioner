from flask_restful import Resource
from flask import jsonify, make_response, request
from ....utils.validators import Validations

from ..models.meetup_models import MeetupRecords, ConfirmRecords

class Meetup(Resource, MeetupRecords):
    def __init__(self):
        self.records = MeetupRecords()
        self.validate = Validations()

    def post(self):
         data = request.get_json()
         data_valid = self.validate.validate_meetup_keys(data)
         if data_valid:

             title = data['title']
             description = data['description']
             venue = data['venue']
             date = data['date']
             res = self.records.save(title, description,venue, date)
             return make_response(jsonify({"A new record with the following data has been added": res}), 201)
         else:
             return make_response(jsonify({"Error":"Unrecognised field"}), 400)

    def get(self):
        res = self.records.get_records()
        return make_response(jsonify({"The available records are": res}), 200)

class MeetupId(Resource, MeetupRecords):
    def __init__(self):
        self.records = MeetupRecords()

    def get(self, id):
        rec = self.records.find(id)
        if rec:
            return make_response(jsonify({"My new records are": rec}), 200)
        else:
            return make_response(jsonify({"Msg": "Meetup record not found"}), 404)

class ConfirmAttendance(ConfirmRecords, Resource):
    def __init__(self):
        self.records = ConfirmRecords()
        self.validate = Validations()

    def get(self, m_id):
        rec = self.records.get_confirms(m_id)
        if rec:
            return make_response(jsonify({"The selected meetup has the following confirmations": rec}), 200)


    def post(self, m_id):
        data = request.get_json()
        data_valid = self.validate.validate_confirm_attendance_keys(data)
        if data_valid:
            meetup_id = m_id
            confirm = data['confirm']
            responce = self.records.save(meetup_id, confirm)
            return make_response(jsonify({"A new confirm Attendance record has been created with the following details": responce}), 201)
        else:
            return make_response(jsonify({"Error":"Unrecognised field"}), 400)
