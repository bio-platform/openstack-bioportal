from flask import request, session
from flask_restful import Resource
from schema import DeleteMetadataSchema, CreateMetadataSchema
from Connection import connect


class Metadata(Resource):

    @staticmethod
    def put(instance_id):
        """
            **Update instance metadata**

            This function allows users to add/update instance metadata.
            Its json input is specified by schema.CreateMetadataSchema

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id or None
            :return: instance information in json and http status code

            - Example::

                  curl -X PUT bio-portal.metacentrum.cz/api/metadata/instance_id/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: ??

                json-format: see openstack.compute.v2.server.Server

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "instance not found"}

        """

        metadata = CreateMetadataSchema().load(request.json)["metadata"]
        connection = connect(session["token"], session["project_id"])
        instance = connection.compute.find_server(instance_id)

        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.set_server_metadata(instance, **metadata)

    @staticmethod
    def get(instance_id):
        """
            **Get instance metadata**

            This function allows users to get instance metadata.

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id or None
            :return: instance information in json and http status code

            - Example::

                  curl -X PUT bio-portal.metacentrum.cz/api/metadata/instance_id/ -H 'Cookie: cookie from scope'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.compute.v2.server.Server

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "instance not found"}

        """
        connection = connect(session["token"], session["project_id"])
        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.get_server_metadata(instance).to_dict(), 200

    @staticmethod
    def delete(instance_id):
        """
            **Get instance metadata**

            This function allows users to remove instance metadata.
            Its json input is specified by schema.DeleteMetadataSchema

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id or None
            :return: empty json and http status code

            - Example::

                curl -X PUT bio-portal.metacentrum.cz/api/metadata/instance_id/ -H 'Cookie: cookie from scope'
                'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 204

                {}

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "instance not found"}

                or

                HTTP Status Code: 400

                {"message": "key not in metadata"}


        """
        connection = connect(session["token"], session["project_id"])
        load = DeleteMetadataSchema().load(request.json)
        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = connection.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in load["keys"]:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        connection.compute.delete_server_metadata(instance, load["keys"])
        return {}, 204
