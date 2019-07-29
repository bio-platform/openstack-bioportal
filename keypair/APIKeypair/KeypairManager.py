from flask_restful import Resource
from keypair.APIKeypair.Keypair import Keypair
from keypair.APIKeypair.KeypairSchema import CreateSchema
from marshmallow import ValidationError
from flask import request


class KeypairManager(Resource):
    def post(self):
        try:
            input = CreateSchema().load(request.json)
            return Keypair().create(**input)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, keypair_id=None):
        if keypair_id is None:
            return Keypair().list()
        else:
            return Keypair().get(keypair_id)

    def put(self):
        return Keypair().update()

    def delete(self):
        return Keypair().delete()

