from flask_restful import Resource
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema
from marshmallow import ValidationError
from flask import request
from VirtualMachineHandler import VirtualMachineHandler
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema
from Security import SecurityGroupRule


class SecurityGroupRuleManager(Resource):
    def post(self):
        try:
            input = SecurityGroupRuleSchema().load(request.json)
            SecurityGroupRule.create(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id=None):
        pass

    def put(self):
        pass

    def delete(self):
        pass
