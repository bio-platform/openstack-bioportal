from flask_restful import Resource
from security_group.APISecurityGroup.SecurityGroupSchema import SecurityGroupRuleSchema
from marshmallow import ValidationError
from flask import request
from VirtualMachineHandler import VirtualMachineHandler
from security_group.APISecurityGroup.SecurityGroup import SecurityGroupRule


class SecurityGroupRuleManager(Resource):
    def post(self, security_group_id):
        try:
            input = SecurityGroupRuleSchema().load(request.json)
            return SecurityGroupRule().create(security_group_id, **input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id, security_group_rule_id=None):
        if security_group_rule_id is None:
            return SecurityGroupRule().list(security_group_rule_id)
        else:
            return SecurityGroupRule().get(security_group_id, security_group_rule_id)

    def put(self, security_group_id):
        return SecurityGroupRule().update(security_group_id)

    def delete(self, security_group_id):
        return SecurityGroupRule().delete(security_group_id)