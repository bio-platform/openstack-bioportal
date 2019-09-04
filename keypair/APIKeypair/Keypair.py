from flask_restful import Resource
from Connection import connect
from flask import session

class Keypair(Resource):
    def helper(self, keyname, public_key, conn):
        if public_key is None:
            return conn.compute.create_keypair(name=keyname)
        return conn.compute.create_keypair(name=keyname, public_key=public_key)

    def create(self,connection, keyname, public_key=None):
        try:
            keypair = connection.compute.find_keypair(keyname)
            if not keypair:
                return self.helper(keyname, public_key, connection), 201

            elif keypair.public_key != public_key:
                connection.compute.delete_keypair(keypair)
                return self.helper(keyname, public_key, connection), 200

            return keypair, 200

        except Exception as e:
            return {"message": "Import Keypair {0} error:{1}".format(keyname, e), "result": {}}, 400

    def update(self, keypair_id):
        return {}, 501

    def delete(self, keypair_id):
        return {}, 501

    def get(self,connection, keypair_id):
        keypair = connection.compute.find_keypair(keypair_id)
        if keypair is None:
            return {}, 404
        return keypair, 200

    def list(self, connection):
        tmp = connection.compute.keypairs()
        return [r for r in tmp], 200
