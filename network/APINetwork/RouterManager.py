from network.APINetwork.Network import Router
from flask_restful import Resource
import DefaultManager
from flask import request


class RouterManager(Resource):

    def get(self, router_id=None):
        if router_id is None:
            return DefaultManager.manage(Router().list, request.json)
        return DefaultManager.manage(Router().get, request.json, router_id=router_id)