from requests import put


class Gateway:

    def add(self,connection, router_id, external_network):
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

    def create(self, connection, instance_id, network_id):
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

            networkID = connection.network.find_network(network_id)
            if networkID is None:

                return {"message":"Network not found"}, 400
            networkID = networkID.to_dict()["id"]
            floating_ip = connection.network.create_ip(floating_network_id=networkID)
            floating_ip = connection.network.get_ip(floating_ip)
            connection.compute.add_floating_ip_to_server(
                server, floating_ip.floating_ip_address
            )
            return floating_ip, 201
        except Exception as e:
            return {"message": "Adding Floating IP to {0} with network {1} error:{2}".format(instance_id, network_id, e)}

    def get(self,connection, floating_ip_id):
        floating_ip = connection.network.get_ip(floating_ip_id)
        if floating_ip is None:
            return {}, 404
        return floating_ip.to_dict(), 200

    def list(self, connection):
        ips = connection.network.ips()
        return [r for r in ips], 200

class Network:
    def get(self, connection, network_id):
        network = connection.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200

    def list(self, connection):
        network = connection.network.networks()
        return [r for r in network], 200

class Router:
    def get(self, router_id):
        pass

    def list(self, connection):
        routers = connection.network.routers()
        return [r for r in routers], 200
