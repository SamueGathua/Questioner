from flask_restful import Api, Resource
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

from .views.user_views import Signup, AuthenticateUser
from .views.meetup_views import Meetup
from .views.question_views import Question

api.add_resource(Signup, '/user/signup')
api.add_resource(AuthenticateUser, '/user/login')
api.add_resource(Meetup, '/meetups')
api.add_resource(Question, '/meetups/<int:id>/questions')
