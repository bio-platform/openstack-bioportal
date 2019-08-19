from Connection import connect
from flask import session


class Limit:
    def list(self):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        limits = conn.compute.get_limits()
        absolute = limits["absolute"]
        res = {"floating_ips": {"limit":absolute["floating_ips"],
                               "used":absolute["floating_ips_used"]},
               "instances": {"limit":absolute["instances"],
                               "used":absolute["instances_used"]},
               "cores": {"limit":absolute["total_cores"],
                               "used":absolute["total_cores_used"]},
               "ram": {"limit":absolute["total_ram"],
                               "used":absolute["total_ram_used"]}}
        return res, 200
