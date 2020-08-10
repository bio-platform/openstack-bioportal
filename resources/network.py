from flask import session
from flask_restful import Resource
from Connection import connect


class Network(Resource):
    @staticmethod
    def get(network_id=None):
        """
            **Get/list network**

            This function allows users to get their network specified by its ID. If no parameter given, all users
            networks are returned

            :param network_id: id of the network
            :type network_id: openstack network id or None
            :return: network/s in json and http status code

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/networks/_your_keypair_id/ -H 'Cookie: cookie from scope'
                -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.network.v2.network.Network

                or

                HTTP Status Code: 200

                openstack.network.v2..network.Network array

            - Expected Fail Response::

                HTTP Status Code: 404

                {}


        """
        connection = connect(session["token"], session["project_id"])
        if network_id is None:
            network = connection.network.networks()
            return [r for r in network], 200
        network = connection.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200
