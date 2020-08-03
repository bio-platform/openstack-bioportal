from flask import request
from flask_restful import Resource

import DefaultManager
from instance.APIInstance.Instance import Instance
from instance.APIInstance.InstanceSchema import StartServerSchema


class InstanceManager(Resource):

    @staticmethod
    def post():
        return DefaultManager.manage(Instance().create, request.json, StartServerSchema)

    @staticmethod
    def get(instance_id=None):
        if instance_id is None:
            return DefaultManager.manage(Instance().list, request.json)
        else:
            return DefaultManager.manage(Instance().get, request.json, instance_id=instance_id)

    @staticmethod
    def put():
        return DefaultManager.manage(Instance().update, request.json)

    @staticmethod
    def delete(instance_id):
        return DefaultManager.manage(Instance().delete, request.json, instance_id=instance_id)
