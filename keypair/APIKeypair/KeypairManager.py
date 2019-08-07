from flask_restful import Resource
from keypair.APIKeypair.Keypair import Keypair
from keypair.APIKeypair.KeypairSchema import CreateSchema
from marshmallow import ValidationError
from flask import request
import DefaultManager


class KeypairManager(Resource):
    def post(self):
        return DefaultManager.manage(Keypair().create, request.json, CreateSchema)

    def get(self, keypair_id=None):
        if keypair_id is None:
            return DefaultManager.manage(Keypair().list, request.json)
        else:
            return DefaultManager.manage(Keypair().list, request.json, keypair_id=keypair_id)

    def put(self):
        return Keypair().update()

    def delete(self):
        return Keypair().delete()

