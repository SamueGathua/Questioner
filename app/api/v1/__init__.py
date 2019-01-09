from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

from .views.meetup_views import Meetup, MeetupId

api.add_resource(Meetup, '/meetups')
api.add_resource(MeetupId, '/meetups/<int:id>')
