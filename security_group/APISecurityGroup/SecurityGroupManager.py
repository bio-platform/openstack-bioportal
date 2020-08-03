from flask_restful import Resource
from security_group.APISecurityGroup.SecurityGroupSchema import SecurityGroupSchema
from flask import request
from security_group.APISecurityGroup.SecurityGroup import SecurityGroup
import DefaultManager


class SecurityGroupManager(Resource):
    @staticmethod
    def post():
        return DefaultManager.manage(SecurityGroup().create, request.json, SecurityGroupSchema)

    @staticmethod
    def get(security_group_id=None):
        if security_group_id is None:
            return DefaultManager.manage(SecurityGroup().list, request.json)
        else:
            return DefaultManager.manage(SecurityGroup().get, request.json, security_group_id=security_group_id)

    @staticmethod
    def put():
        return SecurityGroup().update()

    @staticmethod
    def delete():
        return SecurityGroup().delete()

