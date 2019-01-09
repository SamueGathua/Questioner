from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.confirm_models import ConfirmRecord
class ConfirmAttendance(ConfirmRecord, Resource):
    def __init__(self):
        self.records = ConfirmRecord()

    def post(self, id):
        data = request.get_json()
        meetup_id = id
        confirm = data['confirm']
        responce = self.records.save(meetup_id, confirm)
        return make_response(jsonify({"A new confirm Attendance record has been created with the following details": responce}), 201)
