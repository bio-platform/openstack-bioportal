from flask import session
from flask_restful import Resource

from Connection import connect


class Limit(Resource):
    @staticmethod
    def get():
        """
            **Get resource limits**

            This function allows users to get their resource limits and their usage.

            :return: limit information in json and http status code

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/limits/ -H 'Cookie: cookie from scope'
                -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                {"floating_ips":
                    {"limit": 5,
                     "used" : 2},
                "instances":
                    {"limit": 3,
                     "used" : 1},
                "cores":
                    {"limit": 16,
                     "used" : 6},
                "ram":
                    {"limit": 4,
                     "used" : 1},
                }

            - Expected Fail Response::

                HTTP Status Code: 400

                {}

        """
        connection = connect(session["token"], session["project_id"])
        limits = connection.compute.get_limits()
        absolute = limits["absolute"]
        res = {"floating_ips": {"limit": absolute["floating_ips"],
                                "used": absolute["floating_ips_used"]},
               "instances": {"limit": absolute["instances"],
                             "used": absolute["instances_used"]},
               "cores": {"limit": absolute["total_cores"],
                         "used": absolute["total_cores_used"]},
               "ram": {"limit": absolute["total_ram"],
                       "used": absolute["total_ram_used"]}}
        return res, 200

