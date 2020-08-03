from flask_restful import Resource


class Keypair(Resource):

    @staticmethod
    def create(connection, key_name, public_key=None):
        try:
            key_pair = connection.compute.find_keypair(key_name)
            if not key_pair:
                return connection.compute.create_keypair(key_name, public_key), 201

            elif key_pair.public_key != public_key:
                connection.compute.delete_keypair(key_pair)
                return connection.compute.create_keypair(key_name, public_key), 200

            return key_pair, 200

        except Exception as e:
            return {"message": "Import Keypair {0} error:{1}".format(key_name, e), "result": {}}, 400

    @staticmethod
    def update(key_pair_id):
        return {}, 501

    @staticmethod
    def delete(key_pair_id):
        return {}, 501

    @staticmethod
    def get(connection, key_pair_id):
        key_pair = connection.compute.find_keypair(key_pair_id)
        if key_pair is None:
            return {}, 404
        return key_pair, 200

    @staticmethod
    def list(connection):
        tmp = connection.compute.keypairs()
        return [r for r in tmp], 200
