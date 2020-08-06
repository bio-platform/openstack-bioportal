from flask_restful import Resource
from flask import session
from requests import get
from flask import current_app as app


class Project(Resource):
    @staticmethod
    def get():
        app.logger.info("project call - " + str(session))
        projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % session['user_id'],
                       headers={"Accept": "application/json",
                                "User-Agent": "Mozilla/5.0 (X11;\
                                                    Ubuntu; Linux x86_64; rv:68.0)\
                                                    Gecko/20100101 Firefox/68.0",
                                "X-Auth-Token": session['token']})
        if projects.json():
            return projects.json(), 200
        return {}, 400
