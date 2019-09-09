from login.APILogin.Login import Login
from login.APILogin.LoginSchema import ScopeSchema, LoginSchema
from flask_restful import Resource
from flask import request, session
from marshmallow import ValidationError

class LoginManager(Resource):

    def post(self):
        try:
            load = LoginSchema().load(request.json)
            return Login().login(**load)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400

    def get(self):
        return Login().list()

    def put(self):
        try:
            load = ScopeSchema().load(request.json)
            return Login().scope(**load)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400