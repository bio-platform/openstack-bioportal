from flask_restful import Resource
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema
from marshmallow import ValidationError
from flask import request
from VirtualMachineHandler import VirtualMachineHandler
from security.APISecurity.SecuritySchema import SecurityGroupRuleSchema


class SecurityGroupRuleManager(Resource):
    vh = VirtualMachineHandler("token", "clouds.yaml")

    def post(self):
        try:
            input = SecurityGroupRuleSchema().load(request.json)
            self.vh.add_security_group_rule(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id=None):
        if security_group_id is None:
            return self.vh.list_security_groups()
        else:
            return self.vh.get_security_group(security_group_id)

    def put(self):
        pass

    def delete(self):
        pass
