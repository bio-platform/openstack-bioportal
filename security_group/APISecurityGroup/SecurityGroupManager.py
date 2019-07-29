from flask_restful import Resource
from security_group.APISecurityGroup.SecurityGroupSchema import SecurityGroupSchema
from marshmallow import ValidationError
from flask import request
from security_group.APISecurityGroup.SecurityGroup import SecurityGroup



class SecurityGroupManager(Resource):
    def post(self):
        try:
            input = SecurityGroupSchema().load(request.json)
            return SecurityGroup().create(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, security_group_id=None):
        if security_group_id is None:
             return SecurityGroup().list()
        else:
            return SecurityGroup().get(security_group_id)

    def put(self):
        return SecurityGroup().update()

    def delete(self):
        return SecurityGroup().delete()

