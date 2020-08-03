from flask import request
from flask_restful import Resource

import DefaultManager
from network.APINetwork.Network import Network


class NetworkManager(Resource):

    def get(self, network_id=None):
        if network_id is None:
            return DefaultManager.manage(Network().list, request.json)
        return DefaultManager.manage(Network().get, request.json, network_id=network_id)
