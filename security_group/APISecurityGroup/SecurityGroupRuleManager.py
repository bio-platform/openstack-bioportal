from flask_restful import Resource
from security_group.APISecurityGroup.SecurityGroupSchema import SecurityGroupRuleSchema
from flask import request
from security_group.APISecurityGroup.SecurityGroup import SecurityGroupRule
import DefaultManager


class SecurityGroupRuleManager(Resource):
    def post(self, security_group_id):
        return DefaultManager.manage(SecurityGroupRule().create,
                      request.json,
                      SecurityGroupRuleSchema,
                      security_group_id=security_group_id)

    def get(self, security_group_id, security_group_rule_id=None):
        if security_group_rule_id is None:
            return  DefaultManager.manage(SecurityGroupRule().list,
                          request.json,
                          security_group_id=security_group_id)
        else:
            return DefaultManager.manage(SecurityGroupRule().get,
                          request.json,
                          security_group_rule_id=security_group_rule_id,
                          security_group_id=security_group_id)

    def put(self, security_group_id):
        return DefaultManager.manage(SecurityGroupRule().update,request.json, security_group_id=security_group_id)

    def delete(self, security_group_id):
        return DefaultManager.manage(SecurityGroupRule().delete,request.json, security_group_id=security_group_id)
