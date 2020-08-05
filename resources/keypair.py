from flask import request, session
from flask_restful import Resource
from schemas.KeypairSchema import CreateSchema
from Connection import connect


class Keypair(Resource):

    @staticmethod
    def post():
        connection = connect(session["token"], session["project_id"])
        load = CreateSchema().load(request.json)
        key_pair = connection.compute.find_keypair(load["key_name"])
        if not key_pair:
            return connection.compute.create_keypair(**load), 201

        elif key_pair.public_key != load["public_key"]:
            connection.compute.delete_keypair(key_pair)
            return connection.compute.create_keypair(**load), 200
        return key_pair, 200

    @staticmethod
    def get(keypair_id=None):
        connection = connect(session["token"], session["project_id"])
        if keypair_id is None:
            tmp = connection.compute.keypairs()
            return [r for r in tmp], 200
        else:
            key_pair = connection.compute.find_keypair(keypair_id)
            if key_pair is None:
                return {}, 404
            return key_pair, 200
