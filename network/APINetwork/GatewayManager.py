from network.APINetwork.NetworkSchema import NetworkSchema
from marshmallow import ValidationError
from flask import request
from network.APINetwork.Network import Gateway
from flask_restful import Resource


class GatewayManager(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self, router_id):
        try:
            input = NetworkSchema().load(request.json)
            return Gateway().add(router_id, **input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def delete(self):
        pass


