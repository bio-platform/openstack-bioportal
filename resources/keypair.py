from flask import request, session
from flask_restful import Resource
from schema import CreateKeypairSchema
from Connection import connect


class Keypair(Resource):

    @staticmethod
    def post():
        """
            **Add new public key**

            This function allows users to add new public key. If keypair with given name doesnt exist, its created.
            In case keypair with same name exits and their keys are different, old key is deleted and new one is created.
            Otherwise returns keypair that already existed is returned

            Its json input is specified by schema.CreateKeypairSchema

            :return: keypair information in json and http status code

            - Example::

                  curl -X POST bio-portal.metacentrum.cz/api/keypairs/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.compute.v2.server

                or

                HTTP Status Code: 201

                json-format: see openstack.compute.v2.server

            - Expected Fail Response::

                HTTP Status Code: 400

                {}


        """
        connection = connect(session["token"], session["project_id"])
        load = CreateKeypairSchema().load(request.json)
        key_pair = connection.compute.find_keypair(load["key_name"])
        if not key_pair:
            return connection.compute.create_keypair(**load), 201

        elif key_pair.public_key != load["public_key"]:
            connection.compute.delete_keypair(key_pair)
            return connection.compute.create_keypair(**load), 200
        return key_pair, 200

    @staticmethod
    def get(keypair_id=None):
        """
            **Get/list keypair**

            This function allows users to get their instance specified by its ID. If no parameter given, all users instances
            are returned

            :param keypair_id: id of the keypair
            :type keypair_id: openstack keypair id or None
            :return: keypair/s in json and http status code

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/keypairs/_your_keypair_id/ -H 'Cookie: cookie from scope'
                -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.compute.v2.keypair.Keypair

                or

                HTTP Status Code: 200

                openstack.compute.v2.keypair.Keypair array

            - Expected Fail Response::

                HTTP Status Code: 404

                {}


        """
        connection = connect(session["token"], session["project_id"])
        if keypair_id is None:
            tmp = connection.compute.keypairs()
            return [r for r in tmp], 200
        else:
            key_pair = connection.compute.find_keypair(keypair_id)
            if key_pair is None:
                return {}, 404
            return key_pair, 200
