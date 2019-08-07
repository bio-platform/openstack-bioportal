from flask_restful import Resource
from security_group.APISecurityGroup.SecurityGroupSchema import SecurityGroupSchema
from flask import request
from security_group.APISecurityGroup.SecurityGroup import SecurityGroup
import DefaultManager


class SecurityGroupManager(Resource):
    def post(self):
        return DefaultManager.manage(SecurityGroup().create, request.json, SecurityGroupSchema)

    def get(self, security_group_id=None):
        if security_group_id is None:
            return DefaultManager.manage(SecurityGroup().list, request.json)
        else:
            return DefaultManager.manage(SecurityGroup().get, request.json, security_group_id=security_group_id)

    def put(self):
        return SecurityGroup().update()

    def delete(self):
        return SecurityGroup().delete()

