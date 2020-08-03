from requests import put


class Gateway:
    @staticmethod
    def add(connection, router_id, external_network):
        router = connection.network.find_router(router_id)
        if not router:
            return {"message": "Wrong router ID, router not found!"}, 400

        router_gateway_request = {"router":
            {
                "external_gateway_info": {
                    "network_id": external_network
                }
            }
        }
        return put("https://network.cloud.muni.cz/v2.0/routers/%s" % router_id,
                   headers={"X-Auth-Token": connection.authorize()}, json=router_gateway_request).json()


class FloatingIp:
    @staticmethod
    def create(connection, instance_id, network_id):
        try:
            server = connection.compute.find_server(instance_id)
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

            network = connection.network.find_network(network_id)
            if network is None:
                return {"message": "Network not found"}, 400
            found_network_id = network.to_dict()["id"]
            floating_ip = connection.network.create_ip(floating_network_id=found_network_id)
            floating_ip = connection.network.get_ip(floating_ip)
            connection.compute.add_floating_ip_to_server(
                server, floating_ip.floating_ip_address
            )
            return floating_ip, 201
        except Exception as e:
            return {
                "message": "Adding Floating IP to {0} with network {1} error:{2}".format(instance_id, network_id, e)}

    @staticmethod
    def get(connection, floating_ip_id):
        floating_ip = connection.network.get_ip(floating_ip_id)
        if floating_ip is None:
            return {}, 404
        return floating_ip.to_dict(), 200

    @staticmethod
    def list(connection):
        ips = connection.network.ips()
        return [r for r in ips], 200


class Network:
    @staticmethod
    def get(connection, network_id):
        network = connection.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200

    @staticmethod
    def list(connection):
        network = connection.network.networks()
        return [r for r in network], 200


class Router:
    @staticmethod
    def get(router_id):
        pass

    @staticmethod
    def list(connection):
        routers = connection.network.routers()
        return [r for r in routers], 200
