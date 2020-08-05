from flask import session
from flask_restful import Resource

from Connection import connect


class Router(Resource):

    @staticmethod
    def get(router_id=None):
        if router_id is None:
            connection = connect(session["token"], session["project_id"])
            routers = connection.network.routers()
            return [r for r in routers], 200
        return {}, 501
