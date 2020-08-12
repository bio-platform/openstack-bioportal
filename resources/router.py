from flask import session
from flask_restful import Resource

from Connection import connect


class Router(Resource):

    @staticmethod
    def get(router_id=None):
        """
                **Get router**

                This function allows users to get their router specified by its ID (not implemented).
                If no parameter given, all users routers are returned

                :param router_id: id of the cloud router
                :type router_id: openstack router id or None
                :return: router/s information in json and http status code

                - Example::

                    curl -X GET http://bio-portal.metacentrum.cz/api/routers/ -H 'Cookie: cookie from scope'
                -
                 Expected Success Response::

                    HTTP Status Code: 200

                    openstack.network.v2.router array

                - Expected Fail Response::

                    HTTP Status Code: 404

                    {}

                    or

                    HTTP Status Code: 501

                    {}



            """
        if router_id is None:
            connection = connect(session["token"], session["project_id"])
            routers = connection.network.routers()
            return [r for r in routers], 200
        return {}, 501
