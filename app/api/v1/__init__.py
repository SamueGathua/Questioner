from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

from .views.meetup_views import Meetup, MeetupId
from .views.question_views import Question
from .views.confirm_views import ConfirmAttendance
from .views.voting_views import Voting
from .views.signup_views import Signup

api.add_resource(Meetup, '/meetups')
api.add_resource(Signup, '/signup')
api.add_resource(MeetupId, '/meetups/<int:id>')
api.add_resource(Question, '/meetups/<int:id>/questions')
api.add_resource(ConfirmAttendance, '/meetups/<int:id>/confirms')
api.add_resource(Voting, '/meetups/questions/<int:id>/votes')
