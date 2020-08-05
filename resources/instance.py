"""
.. module:: Instance
   :synopsis: All endpoints of the Teacher API are defined here
.. moduleauthor:: Rich Yap <github.com/richyap13>
"""

import base64

from oslo_utils import encodeutils

from flask import request, session, jsonify
from flask_restful import Resource

from schemas.InstanceSchema import StartServerSchema
from Connection import connect


class Instance(Resource):

    @staticmethod
    def post():
        """POST method"""
        return Instance._create(connect(session['token'],session['project_id']),
                                **StartServerSchema().load(request.json))
    @staticmethod
    def get(instance_id=None):
        """GET method"""

        connection = connect(session['token'], session['project_id'])
        import json
        if instance_id is not None:
            server = connection.compute.find_server(instance_id)
            json.dumps(server)
            if server is None:
                return {}, 404

            return server, 201
        else:
            tmp = connection.compute.servers()
            return [r for r in tmp], 200


    @staticmethod
    def delete(instance_id):
        """DELETE method"""
        connection = connect(session['token'], session['project_id'])
        server = connection.compute.find_server(instance_id)
        if server is None:
            return {}, 400
        connection.compute.delete_server(instance_id)
        return {}, 204

    @staticmethod
    def _create(connection,
               flavor,
               image,
               key_name,
               servername,
               network_id,
               metadata,
               diskspace=None,
               volume_name=None
               ):

        image = connection.compute.find_image(image)
        flavor = connection.compute.find_flavor(flavor)
        network = connection.network.find_network(network_id)
        key_pair = connection.compute.find_keypair(key_name)
        with open("cloud-init-bioconductor-image.sh", "r") as file:
            text = file.read()
            text = encodeutils.safe_encode(text.encode("utf-8"))
        init_script = base64.b64encode(text).decode("utf-8")

        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400
        server = connection.compute.create_server(
            name=servername,
            image_id=image.id,
            flavor_id=flavor.id,
            networks=[{"uuid": network.id}],
            key_name=key_pair.name,
            metadata=metadata,
            user_data=init_script
        )
        return server, 201
