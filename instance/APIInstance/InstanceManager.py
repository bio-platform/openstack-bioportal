from flask_restful import Resource
from instance.APIInstance.Instance import Instance
from instance.APIInstance.InstanceSchema import StartServerSchema
from marshmallow import ValidationError
from flask import request


class InstanceManager(Resource):
    def post(self):
        try:
            input = StartServerSchema().load(request.json)
            return Instance().create(**input)

        except ValidationError as VE:

            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, instance_id=None):
        if instance_id is None:
            return Instance().list("token")
        else:
            return Instance().get(instance_id,"token")

    def put(self):
        return Instance().update()

    def delete(self):
        return Instance().delete()
