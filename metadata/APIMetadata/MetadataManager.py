from flask import request
from flask_restful import Resource

import DefaultManager
from metadata.APIMetadata.Metadata import Metadata
from metadata.APIMetadata.MetadataSchema import DeleteSchema, CreateSchema


class MetadataManager(Resource):
    @staticmethod
    def post():
        pass

    @staticmethod
    def put(instance_id):
        return DefaultManager.manage(Metadata().set, request.json, CreateSchema, instance_id=instance_id)

    @staticmethod
    def get(instance_id):
        return DefaultManager.manage(Metadata().get, request.json, instance_id=instance_id)

    @staticmethod
    def delete(instance_id):
        return DefaultManager.manage(Metadata().delete, request.json, DeleteSchema, instance_id=instance_id)
