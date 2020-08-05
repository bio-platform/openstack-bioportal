from flask import session as flask_session
from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from openstack import connection

from Connection import connect
from openstack_resources import AUTH_URL, IDENTITY_PROVIDER, PROTOCOL
import logging

class Login:

    def login(self, token):

        admin = OidcAccessToken(auth_url=AUTH_URL,
                                identity_provider=IDENTITY_PROVIDER,
                                protocol=PROTOCOL,
                                access_token=token)

        sess = session.Session(auth=admin)
        conn = connection.Connection(session=sess)
        unscoped_token = conn.authorize()

        user_id = admin.get_user_id(sess)
        logging.debug("my debug output" + str(user_id))
        flask_session['token'] = unscoped_token
        flask_session['user_id'] = user_id
        flask_session.permanent = True
        return {}, 200
        # return {'message': 'no project for user'}, 400

    def list(self):
        if 'project_id' in flask_session and 'token' in flask_session:
            return {'project_id': flask_session['project_id'], 'token': flask_session['token']}, 200
        return {'message': 'unauthorized'}, 401

    def scope(self, project_id):
        try:
            connect(flask_session['token'], project_id)
        except:
            return {'message': 'connection error'}, 401

        flask_session["project_id"] = project_id
        return {}, 204
