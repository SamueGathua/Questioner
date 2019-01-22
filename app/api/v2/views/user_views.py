from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from ..models.user_models import UserRecords
from ....utils.validators import Validations

class Signup(Resource, UserRecords):
    def __init__(self):
        self.records = UserRecords()
        self.parser = reqparse.RequestParser()
        self.validate = Validations()
        """validates the key and data types  for the meetup record"""
        self.parser.add_argument('firstname', type=str, required=True, help='Invalid key for firstname')
        self.parser.add_argument('lastname', type=str, required=True, help='Invalid key for flask_restfulname')
        self.parser.add_argument('othername', type=str, required=True, help='Invalid key for othername')
        self.parser.add_argument('email', type=str, required=True, help='Invalid key for email')
        self.parser.add_argument('phonenumber', type=str, required=True, help='Invalid key for phonenumber')
        self.parser.add_argument('password', type=str, required=True, help='Invalid key for password')
        self.parser.add_argument('isadmin', type=bool, help='Invalid key for isadmin')


    def post(self):
         data = self.parser.parse_args(strict=True)
         """Checks that the fields are not empty"""
         if not data:
             return make_response(jsonify({"status":400,
                                        "Error":" All the fields are required"}), 400)
         if not data['firstname'] or not data['firstname'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":" The firstname field is required"}), 400)
         if not data['lastname'] or  not data['firstname'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":"The lastname field is required"}), 400)
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
         if not self.validate.validate_password(data['password']):
             return make_response(jsonify({"status":400,
                                        "Error":"Password should have atleast 1 character,1 uppercase,and \
                                         a number"}), 400)

         else:
             access_token = create_access_token(identity=data['email'])
             res = self.records.save(data)
             return make_response(jsonify({
                                        "message": "Records for {} {} has beed added \
                                        to the database".format( data['firstname'],data['lastname']),
                                        "Token":access_token}), 201)


class AuthenticateUser(UserRecords, Resource):
    """ class to login a user """
    def __init__(self):
        self.rec = UserRecords()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Invalid key for Email')
        self.parser.add_argument('password', type=str, required=True, help='Invalid key for Password')

    def post(self):
        """ post request endpoint for user login """
        data= self.parser.parse_args(strict=True)

        if not data['email'].strip():
            return make_response(jsonify({"status":400,
                                       "Error":"Email field is required"}), 400)
        if not data['password'].strip():
            return make_response(jsonify({"status":400,
                                       "Error":"Password field is required"}), 400)

        user_data = self.rec.login_user(data['email'])
        if user_data:
            password,email = user_data
            access_token = create_access_token(identity= email.strip())
            if check_password_hash(password.strip(), data['password']):

                return make_response(jsonify({"message":"Login for {} succesful".format(data['email']),
                                             "Token":access_token}), 200)
            else:
                return make_response(jsonify({"message":"Incorrect password"}), 400)

        return make_response(jsonify({"message":"User does not exist"}), 404)
