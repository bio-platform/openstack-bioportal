from flask import Flask
from flask_restful import Api
from network.APINetwork.GatewayManager import GatewayManager
from network.APINetwork.FloatingIpManager import FloatingIpManager
from network.APINetwork.NetworkManager import NetworkManager

app = Flask(__name__)
api = Api(app)

api.add_resource(GatewayManager, '/gateway/', '/gateway/<string:router_id>/')
api.add_resource(FloatingIpManager, '/floating_ip/', '/floating_ip/<string:floating_ip_id>/')
api.add_resource(NetworkManager, '/', '/<string:network_id>/')

if __name__ == '__main__':
    app.run(debug=True)