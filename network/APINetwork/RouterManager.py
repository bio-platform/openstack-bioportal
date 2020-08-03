from flask import request
from flask_restful import Resource

import DefaultManager
from network.APINetwork.Network import Router


class RouterManager(Resource):

    def get(self, router_id=None):
        if router_id is None:
            return DefaultManager.manage(Router().list, request.json)
        return DefaultManager.manage(Router().get, request.json, router_id=router_id)
