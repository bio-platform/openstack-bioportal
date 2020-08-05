from flask import session
from flask_restful import Resource
from Connection import connect


class Network(Resource):
    @staticmethod
    def get(network_id=None):
        connection = connect(session["token"], session["project_id"])
        if network_id is None:
            network = connection.network.networks()
            return [r for r in network], 200
        network = connection.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200
