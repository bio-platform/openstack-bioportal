from flask_restful import Resource
from flask import request
from metadata.APIMetadata.Metadata import Metadata
from metadata.APIMetadata.MetadataSchema import DeleteSchema, CreateSchema
import DefaultManager


class MetadataManager(Resource):
    def post(self):
        pass

    def put(self, instance_id):
        return DefaultManager.manage(Metadata().set, request.json, CreateSchema, instance_id=instance_id)

    def get(self, instance_id):
        return DefaultManager.manage(Metadata().get, request.json, instance_id=instance_id)

    def delete(self, instance_id):
        return DefaultManager.manage(Metadata().delete, request.json, DeleteSchema, instance_id=instance_id)
