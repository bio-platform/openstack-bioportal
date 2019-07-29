from network.APINetwork.Network import Network
from flask_restful import Resource


class NetworkManager(Resource):

    def get(self, network_id=None):
        if network_id is None:
            return Network().list()
        return Network().get(network_id)