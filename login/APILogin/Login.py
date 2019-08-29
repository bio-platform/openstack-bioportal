from flask import session as flask_session
from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from openstack import connection
from requests import get
from openstack_resources import AUTH_URL, IDENTITY_PROVIDER, PROTOCOL


class Login:

    def post(self, json):

        if json and 'token' in json:
            admin = OidcAccessToken(auth_url=AUTH_URL,
                                    identity_provider=IDENTITY_PROVIDER,
                                    protocol=PROTOCOL,
                                    access_token=json['token'])

            sess = session.Session(auth=admin)
            conn = connection.Connection(session=sess)
            unscoped_token = conn.authorize()

            user_id = admin.get_user_id(sess)

            projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % user_id,
                           headers={"Accept": "application/json",
                                    "User-Agent": "Mozilla/5.0 (X11;\
                                    Ubuntu; Linux x86_64; rv:68.0)\
                                    Gecko/20100101 Firefox/68.0",
                                    "X-Auth-Token": unscoped_token}).json()
            if projects["projects"] and 'id' in projects["projects"][0]:
                flask_session['project_id'] = projects["projects"][0]['id']
                flask_session['token'] = unscoped_token
                flask_session.permanent = True

                return {}, 200
            return {'message': 'no project for user'}, 400
        return {'message': 'Could not verify!'}, 401

    def get(self):
        if 'project_id' in flask_session and 'token' in flask_session:
            return {'project_id': flask_session['project_id'], 'token': flask_session['token']},200
        return {'message': 'unauthorized'}, 401
