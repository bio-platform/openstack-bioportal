"""
.. module:: login
   :synopsis: All endpoints of the Teacher API are defined here
.. moduleauthor:: Andrej Cermak <github.com/andrejcermak>
"""

from flask import request
from flask_restful import Resource
from flask import session as flask_session
from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from openstack import connection

from Connection import connect
from schema import ScopeSchema, LoginSchema
from openstack_resources import AUTH_URL, IDENTITY_PROVIDER, PROTOCOL
from flask import current_app as app


class Login(Resource):
    @staticmethod
    def post():
        """
            **Login to portal**

            This function allows users to login to portal using their token.

            :return: empty json and http status code

            - Example::

                  curl -v POST bio-portal.metacentrum.cz/api/
                  -H 'content-type: application/json' --data '{"token": your_token}'

            - Expected Success Response::

                HTTP Status Code: 200

                {}
        """
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
        """
            **Verify your login**

            This function allows users to verify their login.

            :return: json and http status code

            - Example::

                  curl -X GET bio-portal.metacentrum.cz/api/ -H 'Cookie: cookie returned by scope'

            - Expected Success Response::

                HTTP Status Code: 200

                {"project_id": project_id, "token": token}

            - Expected Fail Response::

                HTTP Status Code: 401

                {'message': reason}

        """
        if 'project_id' in flask_session and 'token' in flask_session:
            connect(flask_session["token"], flask_session["project_id"])
            return {'project_id': flask_session['project_id'], 'token': flask_session['token']}, 200
        return {'message': 'unauthorized'}, 401

    @staticmethod
    def put():
        """
            **Scope to project**

            This function allows users to scope to their chosen project.
            Its json input is specified by :class:`~schema.ScopeSchema`

            :return: {} and http status code

            - Example::

                  curl -X PUT bio-portal.metacentrum.cz/api/ -H 'Cookie: cookie returned by login'
                   -H 'content-type: application/json' --data '{"project_id": project_id}'

            - Expected Success Response::

                HTTP Status Code: 204

                {}

            - Expected Fail Response::

                HTTP Status Code: 401

                {'message': 'unauthorized'}

        """
        load = ScopeSchema().load(request.json)
        connect(flask_session['token'], load["project_id"])
        flask_session["project_id"] = load["project_id"]
        return {}, 204
