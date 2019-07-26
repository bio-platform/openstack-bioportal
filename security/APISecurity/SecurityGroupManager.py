from flask_restful import Resource
from keypair.APIKeypair.Keypair import Keypair
from security.APISecurity.SecuritySchema import SecurityGroupSchema
from marshmallow import ValidationError
from flask import request
from VirtualMachineHandler import VirtualMachineHandler


class SecurityGroupManager(Resource):
    vh = VirtualMachineHandler("token", "clouds.yaml")
    def post(self):
        try:
            input = SecurityGroupSchema().load(request.json)
            return self.vh.create_security_group(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id=None):
        pass

    def put(self):
        pass

    def delete(self):
        pass
