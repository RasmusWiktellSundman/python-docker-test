from flask import Flask
from flask_restx import Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

auth = HTTPBasicAuth()
api = Api(app)
from .common import auth_utils

from .resources import test
api.add_resource(test.Test, '/test/<message>')
api.add_resource(test.Test, '/bingoo/is/<message>')
api.add_resource(test.Test, '/thenerdyhamster/is/<message>')
