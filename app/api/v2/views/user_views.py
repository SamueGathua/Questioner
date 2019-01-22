from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from ..models.user_models import UserRecords
from ....utils.validators import Validations

class Signup(Resource, UserRecords):
    def __init__(self):
        self.records = UserRecords()
        self.parser = reqparse.RequestParser()
        self.validate = Validations()

        #validates the key and data types  for the meetup record

        self.parser.add_argument('fname', type=str, required=True, help='Invalid key for fname')
        self.parser.add_argument('lname', type=str, required=True, help='Invalid key for lname')
        self.parser.add_argument('othername', type=str, required=True, help='Invalid key for othername')
        self.parser.add_argument('email', type=str, required=True, help='Invalid key for email')
        self.parser.add_argument('phonenumber', type=str, required=True, help='Invalid key for phonenumber')
        self.parser.add_argument('password', type=str, required=True, help='Invalid key for password')
        self.parser.add_argument('isadmin', type=bool, help='Invalid key for isadmin')


    def post(self):
         data = self.parser.parse_args(strict=True)
         if not data['fname'] or not data['fname'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":" The fname field is required"}), 400)
         if not data['lname'] or  not data['lname'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":"The lname field is required"}), 400)
         if not data['othername'] or not data['othername'].strip() :
             return make_response(jsonify({"status":400,
                                        "Error":"The othername field is required"}), 400)
         if not data['email'] or not data['email'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":"The email field is required"}), 400)
         if not data['phonenumber'] or not data['phonenumber'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":"The phoneNumber field is required"}), 400)
         if not data['password'] or not data['password'].strip():
             return make_response(jsonify({"status":400,
                                       "Error":"The password field is required"}), 400)
         if not self.validate.validate_email(data['email']):
             return make_response(jsonify({"status":400,
                                        "Error":"Invalid email format"}), 400)
         if self.validate.validate_password(data['password']):
             return make_response(jsonify({"status":400,
                                        "Error":"Password should have atleast 1 character,,1 uppercase,and a number"}), 400)

         else:
             res = self.records.save(data)
             return make_response(jsonify({"message":"A new record with the following data has been succesfully added to the database",
                                       "data": res}), 201)
