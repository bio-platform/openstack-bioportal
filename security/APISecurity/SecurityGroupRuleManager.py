from flask_restful import Resource
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema
from marshmallow import ValidationError
from flask import request
from VirtualMachineHandler import VirtualMachineHandler
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema
from security.APISecurity.Security import SecurityGroupRule


class SecurityGroupRuleManager(Resource):
    def post(self):
        try:
            input = SecurityGroupRuleSchema().load(request.json)
            return SecurityGroupRule().create(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id=None):
        if security_group_id is None:
            return SecurityGroupRule().list()
        else:
            return SecurityGroupRule().get(security_group_id)

    def put(self, security_group_id):
        return SecurityGroupRule().update(security_group_id)

    def delete(self, security_group_id):
        return SecurityGroupRule().delete(security_group_id)