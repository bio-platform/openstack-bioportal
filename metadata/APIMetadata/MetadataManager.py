from flask_restful import Resource
from flask import request
from metadata.APIMetadata.Metadata import Metadata
from metadata.APIMetadata.MetadataSchema import DeleteSchema
from marshmallow import ValidationError


class MetadataManager(Resource):
    def post(self):
        pass
    def put(self, instance_id):
        return Metadata().set(instance_id, request.json)
        pass
    def get(self, instance_id):
        return Metadata().get(instance_id)
    def delete(self, instance_id):
        try:
            input = DeleteSchema().load(request.json)
            return Metadata().delete(instance_id, input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400