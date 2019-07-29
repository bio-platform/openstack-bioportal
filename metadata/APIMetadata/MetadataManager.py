from flask_restful import Resource
from flask import request
from metadata.APIMetadata.Metadata import Metadata

class MetadataManager(Resource):
    def post(self):
        pass
    def put(self, instance_id):
        # TODO schema + load
        return Metadata().set(instance_id, request.json)
        pass
    def get(self, instance_id):
        return Metadata().get(instance_id)
    def delete(self, instance_id):
        return Metadata().delete(instance_id, request.json)