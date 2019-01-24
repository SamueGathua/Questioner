from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.comments_models import CommentsRecords
from ..models.base_models import User

class Comments(Resource, CommentsRecords):
    def __init__(self):
        self.records = CommentsRecords()
        self.check_exist = User()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('comment', type=str, required=True, help='Invalid  key for comment')
    @jwt_required
    def post(self, q_id):

        data = self.parser.parse_args(strict=True)
        author = get_jwt_identity()
        comment = data['comment']
        """checks that the data received is not null"""
        if not data['comment'].strip():
            return make_response(jsonify({"status":400,
                                        "error":"The field cannot be empty"}), 400)
        if data['comment']:
            if not self.check_exist.check_item_exist(q_id):
                return make_response(jsonify({"status":400,
                                            "error":"The question does not exist"}), 400)
            else:
                responce = self.records.save_comments(q_id, comment, author)
                return make_response(jsonify({"status":201,
                                           "A new comment record has been created with the following details": responce}), 201)
