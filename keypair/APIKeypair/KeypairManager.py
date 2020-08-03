from flask import request
from flask_restful import Resource

import DefaultManager
from keypair.APIKeypair.Keypair import Keypair
from keypair.APIKeypair.KeypairSchema import CreateSchema


class KeypairManager(Resource):

    @staticmethod
    def post():
        return DefaultManager.manage(Keypair().create, request.json, CreateSchema)

    @staticmethod
    def get(key_pair_id=None):
        if key_pair_id is None:
            return DefaultManager.manage(Keypair().list, request.json)
        else:
            return DefaultManager.manage(Keypair().get, request.json, keypair_id=key_pair_id)

    @staticmethod
    def put(key_pair_id):
        return DefaultManager.manage(Keypair().update, request.json, keypair_id=key_pair_id)

    @staticmethod
    def delete(key_pair_id):
        return DefaultManager.manage(Keypair().update, request.json, keypair_id=key_pair_id)
