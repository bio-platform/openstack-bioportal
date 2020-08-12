from flask_restful import Resource
from flask import request, session

from schema import SecurityGroupSchema
from Connection import connect


class SecurityGroup(Resource):
    @staticmethod
    def post():
        """
            **Create new security group**

            This function allows users to create new security group.

            Its json input is specified by schema.SecurityGroupSchema

            :return: security group information in json and http status code

            - Example::

                  curl -X POST bio-portal.metacentrum.cz/api/security_groups/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 201

                json-format: see openstack.compute.v2.server

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": ...}


            """
        connection = connect(session["token"], session["project_id"])
        load = SecurityGroupSchema().load(request.json)
        new_security_group = connection.network.create_security_group(name=load["name"])
        return new_security_group, 201

    @staticmethod
    def get(security_group_id=None):
        """
            **Get/list security group/s**

            This function allows users to get their security group specified by its ID. If no parameter given, all users
            security groups are returned

            :param security_group_id: id of the security group
            :type security_group_id: openstack security group id or None
            :return: security group/s information in json and http status code

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/security_group/_your_sgroup_id/ -H 'Cookie: cookie from scope'
                 -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.network.v2.security_group

                or

                HTTP Status Code: 200

                openstack.network.v2.security_group array

            - Expected Fail Response::

                HTTP Status Code: 404

                {}


        """
        connection = connect(session["token"], session["project_id"])
        if security_group_id is None:
            tmp = connection.network.security_groups()
            return [r for r in tmp], 200
        else:
            security_group = connection.network.find_security_group(security_group_id)
            if security_group is None:
                return {}, 404
            return security_group.to_dict(), 200


