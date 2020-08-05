from flask import request, session
from flask_restful import Resource
from schemas.MetadataSchema import DeleteSchema, CreateSchema
from Connection import connect


class Metadata(Resource):

    @staticmethod
    def put(instance_id):
        metadata = CreateSchema().load(request.json)["metadata"]
        connection = connect(session["token"], session["project_id"])
        instance = connection.compute.find_server(instance_id)

        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.set_server_metadata(instance, **metadata)

    @staticmethod
    def get(instance_id):
        connection = connect(session["token"], session["project_id"])
        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.get_server_metadata(instance).to_dict(), 200

    @staticmethod
    def delete(instance_id):
        connection = connect(session["token"], session["project_id"])
        load = DeleteSchema().load(request.json)
        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = connection.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in load["keys"]:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        connection.compute.delete_server_metadata(instance, load["keys"])
        return {}, 204
