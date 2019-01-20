from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.user_models import UserRecords

class Signup(Resource, UserRecords):
    def __init__(self):
        self.records = UserRecords()

    def post(self):
         data = request.get_json()
         fname = data['fname']
         lname = data['lname']
         email = data['email']
         password = data['password']
         res = self.records.save(fname,lname, email, password)
         return make_response(jsonify({"A new record with the following data has been succesfully added to the database": res}), 201)

class AuthenticateUser(UserRecords, Resource):

    def __init__(self):
        self.rec = UserRecords()


    def post(self):

        data = request.get_json()
        email = data['email']
        password = data['password']
        user = self.rec.login_user(email, password)

        if not user:
            return make_response(jsonify({"status" : 404,
                                          "Error": "The user does not exist"}), 404)
        if user == 'Fail':
            return make_response(jsonify({"status" : 400,
                                          "Message": "Incorrect password"}), 400)
        if user == 'Success':
            return make_response(jsonify({"status" :200,
                                      "Message":"Login is successful"}), 200)
