from flask_restful import Api, Resource
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

from .views.meetup_views import Meetup, MeetupId, ConfirmAttendance
from .views.question_views import Question, Upvotes, Downvotes
from .views.user_views import Signup, AuthenticateUser

api.add_resource(Meetup, '/meetups')
api.add_resource(Signup, '/user/signup')
api.add_resource(AuthenticateUser, '/user/login')
api.add_resource(MeetupId, '/meetups/<int:id>')
api.add_resource(Question, '/meetups/<int:id>/questions')
api.add_resource(ConfirmAttendance, '/meetups/<int:m_id>/confirms')
api.add_resource(Upvotes, '/questions/<int:id>/upvotes')
api.add_resource(Downvotes, '/questions/<int:id>/downvotes')
