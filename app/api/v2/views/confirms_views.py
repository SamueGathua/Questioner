from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.confirms_models import ConfirmRecords

class ConfirmAttendance(Resource, ConfirmRecords):
    def __init__(self):
        self.records = ConfirmRecords()
    @jwt_required
    def post(self, m_id):

        data = request.get_json()
        author = get_jwt_identity()
        confirm = data['confirm']
        #checks that the data received is not null

        if not data['confirm'].strip():
            return make_response(jsonify({"status":400,
                                        "error":"The field cannot be empty"}), 400)
        if data['confirm']:
            if data['confirm'] == "Yes" or data['confirm'] == "No" or data['confirm'] == "Mybe":
                responce = self.records.save(m_id, confirm, author)
                return make_response(jsonify({"status":201,
                                           "A new confirm Attendance record has been created with the following details": responce}), 201)

            return make_response(jsonify({"status":400,
                                    "message":"The valid formats 'Yes' or 'No' or 'Maybe'"}), 201)
