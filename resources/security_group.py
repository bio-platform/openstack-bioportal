from flask_restful import Resource
from flask import request, session

from schema import SecurityGroupSchema
from Connection import connect


class SecurityGroup(Resource):
    @staticmethod
    def post():
        connection = connect(session["token"], session["project_id"])
        load = SecurityGroupSchema().load(request.json)
        new_security_group = connection.network.create_security_group(name=load["name"])
        return new_security_group, 201

    @staticmethod
    def get(security_group_id=None):
        connection = connect(session["token"], session["project_id"])
        if security_group_id is None:
            tmp = connection.network.security_groups()
            return [r for r in tmp], 200
        else:
            security_group = connection.network.find_security_group(security_group_id)
            if security_group is None:
                return {}, 404
            return security_group.to_dict(), 200


