from flask_restful import Resource
from keypair.APIKeypair.Keypair import Keypair
from keypair.APIKeypair.KeypairSchema import CreateSchema
from marshmallow import ValidationError
from flask import request


class KeypairManager(Resource):
    def post(self):
        try:
            input = CreateSchema().load(request.json)
            res = Keypair().create_keypair(input)
            print(res)
        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.field_names), 'result': {}}, 400

    def get(self, keypair_id=None):
        if keypair_id is None:
            return {"message": "ok", "result": Keypair().list_keypairs()}
        else:
            res = Keypair().get_keypair(keypair_id)
            if type(res) == dict:
                return {"message": "ok", "result": res}
            else:
                return {"message": res, "result": {}}, 404

    def put(self):
        pass

    def delete(self):
        pass
