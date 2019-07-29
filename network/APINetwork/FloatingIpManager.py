from network.APINetwork.Network import FloatingIp
from flask_restful import Resource
from network.APINetwork.NetworkSchema import FloatingIpSchema
from flask import request


class FloatingIpManager(Resource):

    def post(self):
        input = FloatingIpSchema().load(request.json)
        return FloatingIp().create(**input)