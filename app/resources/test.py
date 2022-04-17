from flask_restx import Resource, reqparse

from .. import auth

class Test(Resource):

    @auth.login_required
    def get(self, message):
        return message;