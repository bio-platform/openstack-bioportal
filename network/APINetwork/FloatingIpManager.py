from flask import request
from flask_restful import Resource

import DefaultManager
from network.APINetwork.Network import FloatingIp
from network.APINetwork.NetworkSchema import FloatingIpSchema


class FloatingIpManager(Resource):
    @staticmethod
    def post():
        return DefaultManager.manage(FloatingIp().create, request.json, FloatingIpSchema)

    @staticmethod
    def get(floating_ip_id=None):
        if floating_ip_id is None:
            return DefaultManager.manage(FloatingIp().list, request.json)
        return DefaultManager.manage(FloatingIp().get, request.json, floating_ip_id=floating_ip_id)
