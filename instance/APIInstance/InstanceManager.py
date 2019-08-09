from flask_restful import Resource
from instance.APIInstance.Instance import Instance
from instance.APIInstance.InstanceSchema import StartServerSchema
from flask import request
import DefaultManager


class InstanceManager(Resource):

    def post(self):
        return DefaultManager.manage(Instance().create, request.json, StartServerSchema)

    def get(self, instance_id=None):
        if instance_id is None:
            return DefaultManager.manage(Instance().list, request.json)
        else:
            return DefaultManager.manage(Instance().get, request.json, instance_id=instance_id)

    def put(self):
        return DefaultManager.manage(Instance().update, request.json)

    def delete(self):
        return DefaultManager.manage(Instance().update, request.json)
