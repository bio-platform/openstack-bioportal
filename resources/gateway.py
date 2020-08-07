from flask import request, session
from flask_restful import Resource
from requests import put

from schema import NetworkSchema
from Connection import connect


class Gateway(Resource):

    @staticmethod
    def put(router_id):
        connection = connect(session["token"], session["project_id"])
        load = NetworkSchema().load(request.json)
        router = connection.network.find_router(router_id)
        if not router:
            return {"message": "Wrong router ID, router not found!"}, 400

        router_gateway_request = {"router":
            {
                "external_gateway_info": {
                    "network_id": load["external_network"]
                }
            }
        }
        return put("https://network.cloud.muni.cz/v2.0/routers/%s" % router_id,
                   headers={"X-Auth-Token": connection.authorize()}, json=router_gateway_request).json()
