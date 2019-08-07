from network.APINetwork.Network import FloatingIp
from flask_restful import Resource
from network.APINetwork.NetworkSchema import FloatingIpSchema
from flask import request
import DefaultManager


class FloatingIpManager(Resource):

    def post(self):
        return DefaultManager.manage(FloatingIp().create, request.json, FloatingIpSchema)
