from flask import request, session
from flask_restful import Resource
from requests import put

from schema import NetworkSchema
from Connection import connect


class Gateway(Resource):

    @staticmethod
    def put(router_id):
        """
            #TODO prejst co je to za blbost
            **Update gateway**

            This function allows users to add external gateway.
            Its json input is specified by schema.NetworkSchema

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id or None
            :return: router information in json and http status code

            - Example::

                  curl -X PUT bio-portal.metacentrum.cz/api/gateways/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.network.v2.router

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "Wrong router ID, router not found!"}

        """
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
