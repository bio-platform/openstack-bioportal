from flask import request
from flask_restful import Resource
from flask import session as flask_session
from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from openstack import connection

from Connection import connect
from schemas.LoginSchema import ScopeSchema, LoginSchema
from openstack_resources import AUTH_URL, IDENTITY_PROVIDER, PROTOCOL
from flask import current_app as app


class Login(Resource):
    @staticmethod
    def post():
        load = LoginSchema().load(request.json)
        admin = OidcAccessToken(auth_url=AUTH_URL,
                                identity_provider=IDENTITY_PROVIDER,
                                protocol=PROTOCOL,
                                access_token=load["token"])

        sess = session.Session(auth=admin)
        conn = connection.Connection(session=sess)

        unscoped_token = conn.authorize()
        user_id = admin.get_user_id(sess)

        flask_session['token'] = unscoped_token
        flask_session['user_id'] = user_id
        app.logger.info(user_id + " has token: " + unscoped_token)
        flask_session.permanent = True
        return {}, 200

    @staticmethod
    def get():
        if 'project_id' in flask_session and 'token' in flask_session:
            return {'project_id': flask_session['project_id'], 'token': flask_session['token']}, 200
        return {'message': 'unauthorized'}, 401

    @staticmethod
    def put():
        load = ScopeSchema().load(request.json)
        connect(flask_session['token'], load["project_id"])
        flask_session["project_id"] = load["project_id"]
        return {}, 204
