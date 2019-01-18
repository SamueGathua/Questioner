from flask import Flask, Blueprint
from utils.dbconnect import create_tables

from .api.v1 import version_one as v1
from .api.v2 import version_two as v2

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    create_tables()

    return app
