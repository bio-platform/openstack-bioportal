from flask import request, session
from flask_restful import Resource

from Connection import connect
from schema import FloatingIpSchema


class FloatingIp(Resource):

    @staticmethod
    def post():
        """
            **Create new Floating IP**

            This function allows users to add new Floating IP to specified instance.
            If FIP doesnt exist, its created. If already exists and is not attached, then it will be attached to instance

            Its correct json input is specified by schema.FloatingIpSchema

            :return: floating information in json and http status code

            - Example::

                  curl -X GET bio-portal.metacentrum.cz/api/floating_ips/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data: json specified in schema

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.network.v2.floating_ip

                or

                HTTP Status Code: 201

                json-format: see openstack.network.v2.floating_ip

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "Server not found"}

                or

                HTTP Status Code: 400

                {"message": "Network not found"}

        """
        connection = connect(session["token"], session["project_id"])
        load = FloatingIpSchema().load(request.json)
        server = connection.compute.find_server(load["instance_id"])
        if server is None:
            return {"message": "Server not found"}, 400

        for values in server.addresses.values():
            for address in values:
                if address["OS-EXT-IPS:type"] == "floating":
                    return address, 200

        for floating_ip in connection.network.ips():
            if not floating_ip.fixed_ip_address:
                connection.compute.add_floating_ip_to_server(
                    server, floating_ip.floating_ip_address
                )
                return floating_ip.to_dict(), 200

        network = connection.network.find_network(load["network_id"])
        if network is None:
            return {"message": "Network not found"}, 400
        found_network_id = network.to_dict()["id"]
        floating_ip = connection.network.create_ip(floating_network_id=found_network_id)
        floating_ip = connection.network.get_ip(floating_ip)
        connection.compute.add_floating_ip_to_server(
            server, floating_ip.floating_ip_address
        )
        return floating_ip, 201

    @staticmethod
    def get(floating_ip_id=None):
        """
            **Get specific Floating IP**

            This function allows users to get their Floating IP specified by its ID. If no parameter given, all users
            FIPs  are returned

            :param floating_ip_id: id of the floating ip
            :type floating_ip_id: openstack FIP id or None
            :return: FIP/s information in json and http status code

            - Example::

                  curl -X GET bio-portal.metacentrum.cz/api/floating_ips/_your_floating_ip/ -H
                  'Cookie: cookie from scope' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.network.v2.floating_ip

            - Expected Fail Response::

                HTTP Status Code: 404

                {}

        """
        connection = connect(session["token"], session["project_id"])
        if floating_ip_id is None:
            ips = connection.network.ips()
            return [r for r in ips], 200
        floating_ip = connection.network.get_ip(floating_ip_id)
        if floating_ip is None:
            return {}, 404
        return floating_ip.to_dict(), 200
