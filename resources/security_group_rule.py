from flask_restful import Resource
from flask import request, session

from schema import SecurityGroupRuleSchema
from Connection import connect


class SecurityGroupRule(Resource):

    @staticmethod
    def post(security_group_id):
        """
                **Add security group rule**

                This function allows users to add new security group rule.

                Its json input is specified by schema.SecurityGroupRuleSchema

                :param security_group_id: id of the security group id
                :type security_group_id: openstack security group id
                :return: information about created rule in json and http status code

                - Example::

                    curl -X POST bio-portal.metacentrum.cz/api/security_groups/security_group_id/security_group_rule/
                    -H 'Cookie: cookie from scope' -H 'content-type: application/json' --data json_specified_in_schema

                - Expected Success Response::

                    HTTP Status Code: 201

                    json-format: see openstack.network.v2.security_group_rule

                - Expected Fail Response::

                    HTTP Status Code: 409
                    {"message": ...}



            """
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

        if load["type"] == "http":
            new_rule = connection.network.create_security_group_rule(
                direction="ingress",
                protocol="tcp",
                security_group_id=security_group_id,
                ether_type="IPv4",
                port_range_min="80",
                port_range_max="80",
                remote_ip_prefix="0.0.0.0/0")

        if load["type"] == "https":
            new_rule = connection.network.create_security_group_rule(
                direction="ingress",
                protocol="tcp",
                port_range_min="443",
                port_range_max="443",
                security_group_id=security_group_id,
                ether_type="IPv4",
                remote_ip_prefix="0.0.0.0/0")

        if load["type"] == "rdp":
            new_rule = connection.network.create_security_group_rule(
                direction="ingress",
                protocol="tcp",
                port_range_min="3389",
                port_range_max="3389",
                security_group_id=security_group_id,
                ether_type="IPv4",
                remote_ip_prefix="0.0.0.0/0")

        return new_rule.to_dict(), 201


