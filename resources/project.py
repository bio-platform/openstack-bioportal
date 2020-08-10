from flask_restful import Resource
from flask import session
from requests import get
from flask import current_app as app


class Project(Resource):
    @staticmethod
    def get():
        """
                **Get your projects**

                This function allows users to list all their projects.

                :return: all users projects in json and http status code

                - Example::

                    curl -X GET bio-portal.metacentrum.cz/api/projects/ -H 'Cookie: cookie login'
                -
                 Expected Success Response::

                    HTTP Status Code: 200

                    {'links':   {'next': None,
                                'previous': None,
                                'self': 'https://identity.cloud.muni.cz/v3/users/$user_id/projects'},
                                'projects':  [{'description': 'project description',
                                                'domain_id': 'domain id',
                                                'enabled': True,
                                                'id': 'project id',
                                                'is_domain': False,
                                                'links': {'self': 'link to the project'},
                                                'name': 'project name',
                                                'options': {},
                                                'parent_id': 'parent id',
                                                'tags': ['tag']}
                """

        app.logger.info("project call - " + str(session))
        projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % session['user_id'],
                       headers={"Accept": "application/json",
                                "User-Agent": "Mozilla/5.0 (X11;\
                                                    Ubuntu; Linux x86_64; rv:68.0)\
                                                    Gecko/20100101 Firefox/68.0",
                                "X-Auth-Token": session['token']})
        from pprint import pprint
        pprint(projects.json())
        return projects.json(), 200

