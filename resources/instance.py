"""
.. module:: instance
   :synopsis: All endpoints of the Teacher API are defined here
.. moduleauthor:: Andrej Cermak <github.com/andrejcermak>
"""

import base64

from oslo_utils import encodeutils

from flask import request, session
from flask_restful import Resource

from schema import StartServerSchema
from Connection import connect
import requests

class Instance(Resource):

    @staticmethod
    def post():
        """
            **Create new instance**

            This function allows users to start new instance.

            Its json input is specified by schema.StartServerSchema

            :return: instance information in json and http status code

            - Example::

                  curl -X POST bio-portal.metacentrum.cz/api/instances/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 201

                json-format: see openstack.compute.v2.server

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "resoucre not found"}


        """
        connection = connect(session['token'],session['project_id'])
        json = StartServerSchema().load(request.json)
        image = connection.compute.find_image(json["image"])
        flavor = connection.compute.find_flavor(json["flavor"])
        network = connection.network.find_network(json["network_id"])
        key_pair = connection.compute.find_keypair(json["key_name"])

        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400
        path = ""
        if image.name == "debian-10-x86_64_bioconductor":
            req = requests.get("https://raw.githubusercontent.com/bio-platform/bio-class-deb10/main/install/cloud-init-bioconductor-image.sh")
            text = encodeutils.safe_encode(req.text.encode("utf-8"))
            init_script = base64.b64encode(text).decode("utf-8")
        elif image.name == "debian-9-x86_64_bioconductor":
            path = 
            req = requests.get("https://raw.githubusercontent.com/bio-platform/bio-class/master/install/cloud-init-bioconductor-image.sh")
            text = encodeutils.safe_encode(req.text.encode("utf-8"))
            init_script = base64.b64encode(text).decode("utf-8")
        else: 
            init_script = None
        
        server = connection.compute.create_server(
            name=json["servername"],
            image_id=image.id,
            flavor_id=flavor.id,
            networks=[{"uuid": network.id}],
            key_name=key_pair.name,
            metadata=json["metadata"],
            user_data=init_script
        )
        return server, 201

    @staticmethod
    def get(instance_id=None):
        """
            **Get specific instance**

            This function allows users to get their instance specified by its ID. If no parameter given, all users instances
            are returned

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id or None
            :return: instance/s information in json and http status code

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/instances/_your_instance_id/
                 -H 'Cookie: cookie from scope' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.compute.v2.server

                or

                HTTP Status Code: 200

                openstack.compute.v2.server array

            - Expected Fail Response::

                HTTP Status Code: 404

                {}


        """

        connection = connect(session['token'], session['project_id'])
        if instance_id is not None:
            server = connection.compute.find_server(instance_id)
            if server is None:
                return {}, 404

            return server, 200
        else:
            tmp = connection.compute.servers()
            return [r for r in tmp], 200


    @staticmethod
    def delete(instance_id):
        """
            **Delete specific instance**

            This function allows users to delete their instance specified by its ID.

            :param instance_id: id of the cloud instance
            :type instance_id: openstack instance id
            :return: empty json and http status code

            - Example::

                curl -X DELETE bio-portal.metacentrum.cz/api/instances/instance_id/ -H 'Cookie: cookie from scope' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 204

                {}

            - Expected Fail Response::

                HTTP Status Code: 400

                {}


        """
        connection = connect(session['token'], session['project_id'])
        server = connection.compute.find_server(instance_id)
        if server is None:
            return {}, 400
        connection.compute.delete_server(instance_id)
        return {}, 204
