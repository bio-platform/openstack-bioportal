from flask import session
from flask_restful import Resource

from Connection import connect


class Limit(Resource):
    @staticmethod
    def get():
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

