from flask_restful import Resource
from flask import request, session

from schemas.SecurityGroupSchema import SecurityGroupRuleSchema
from Connection import connect


class SecurityGroupRule(Resource):

    @staticmethod
    def post(security_group_id):
        connection = connect(session["token"], session["project_id"])
        load = SecurityGroupRuleSchema().load(request.json)
        if load["type"] == "ssh":
            new_rule = connection.network.create_security_group_rule(
                direction="ingress",
                protocol="tcp",
                port_range_max=22,
                port_range_min=22,
                security_group_id=security_group_id,
                ether_type="IPv4",

            )
        if load["type"] == "all_icmp":
            new_rule = connection.network.create_security_group_rule(
                direction="ingress",
                protocol="ICMP",
                security_group_id=security_group_id,
                ether_type="IPv4",
                remote_ip_prefix="0.0.0.0/0")

        return new_rule.to_dict(), 201


