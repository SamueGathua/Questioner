from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.signup_models import SignupRecords

class Signup(Resource, SignupRecords):
    def __init__(self):
        self.records = SignupRecords()

    def post(self):
         data = request.get_json()

         uname = data['uname']
         email = data['email']
         password = data['password']
         res = self.records.save(uname, email, password)
         return make_response(jsonify({"A new record with the following data has been added": res}), 201)
