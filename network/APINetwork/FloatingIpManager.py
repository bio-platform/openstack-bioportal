from network.APINetwork.Network import FloatingIp
from flask_restful import Resource
from network.APINetwork.NetworkSchema import FloatingIpSchema
from flask import request
import DefaultManager


class FloatingIpManager(Resource):

    def post(self):
        return DefaultManager.manage(FloatingIp().create, request.json, FloatingIpSchema)

    def get(self, floating_ip_id = None):
        if floating_ip_id is None:
            return DefaultManager.manage(FloatingIp().list, request.json)
        return DefaultManager.manage(FloatingIp().get, request.json, floating_ip_id=floating_ip_id)