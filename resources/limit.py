from flask import session
from flask_restful import Resource
from requests import get

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
        quotas = get("https://network.cloud.muni.cz/v2.0/quotas/%s/" % session['project_id'],
                       headers={"Accept": "application/json",
                                "User-Agent": "Mozilla/5.0 (X11;\
                                                            Ubuntu; Linux x86_64; rv:68.0)\
                                                            Gecko/20100101 Firefox/68.0",
                                "X-Auth-Token": connection.authorize()}).json()

        res = {"floating_ips": {"limit": quotas["quota"]["floatingip"],
                                "used": sum(1 for _ in connection.network.ips())},  # get generator length
               "instances": {"limit": absolute["instances"],
                             "used": absolute["instances_used"]},
               "cores": {"limit": absolute["total_cores"],
                         "used": absolute["total_cores_used"]},
               "ram": {"limit": absolute["total_ram"],
                       "used": absolute["total_ram_used"]}}
        return res, 200

