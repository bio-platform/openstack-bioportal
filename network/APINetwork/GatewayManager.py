from network.APINetwork.NetworkSchema import NetworkSchema
from marshmallow import ValidationError
from flask import request
from network.APINetwork.Network import Gateway
from flask_restful import Resource
import DefaultManager

class GatewayManager(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self, router_id):
        return DefaultManager.manage(Gateway().add, request.json, NetworkSchema, router_id=router_id)

    def delete(self):
        pass


