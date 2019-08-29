from login.APILogin.Login import Login
from flask_restful import Resource
from flask import request, session


class LoginManager(Resource):

    def post(self):
        return Login().post(request.json)

    def get(self):
        return Login().get()
