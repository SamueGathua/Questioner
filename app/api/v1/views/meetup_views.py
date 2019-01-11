from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.meetup_models import MeetupRecords, ConfirmRecords

class Meetup(Resource, MeetupRecords):
    def __init__(self):
        self.records = MeetupRecords()

    def post(self):
         data = request.get_json()
         title = data['title']
         description = data['description']
         host = data['host']
         venue = data['venue']
         date = data['date']
         res = self.records.save(title, description, host, venue, date)
         return make_response(jsonify({"A new record with the following data has been added": res}), 201)

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

    def post_confirm(self, id):
        data = request.get_json()
        meetup_id = id
        confirm = data['confirm']
        responce = self.records.save(meetup_id, confirm)
        return make_response(jsonify({"A new confirm Attendance record has been created with the following details": responce}), 201)
