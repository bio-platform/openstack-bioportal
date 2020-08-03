from flask import request
from flask_restful import Resource

import DefaultManager
from network.APINetwork.Network import Gateway
from network.APINetwork.NetworkSchema import NetworkSchema


class GatewayManager(Resource):
    @staticmethod
    def get():
        pass

    @staticmethod
    def post():
        pass

    @staticmethod
    def put(router_id):
        return DefaultManager.manage(Gateway().add, request.json, NetworkSchema, router_id=router_id)

    @staticmethod
    def delete():
        pass
