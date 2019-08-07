from VirtualMachineHandler import VirtualMachineHandler
from requests import put


class Gateway:

    def add(self, token, router_id, external_network):
        vh = VirtualMachineHandler(token)
        router = vh.conn.network.get_router(router_id)
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
                   headers={"X-Auth-Token": vh.conn.authorize()}, json=router_gateway_request).json()

class FloatingIp:

    def create(self, token, instance_id, network_id):
        vh = VirtualMachineHandler(token)
        try:
            server = vh.conn.compute.get_server(instance_id)
            if server is None:
                return {"message": "Server not found"}, 400

            for values in server.addresses.values():
                for address in values:
                    if address["OS-EXT-IPS:type"] == "floating":
                        return address["addr"], 200

            for floating_ip in vh.conn.network.ips():
                if not floating_ip.fixed_ip_address:
                    vh.conn.compute.add_floating_ip_to_server(
                        server, floating_ip.floating_ip_address
                    )

                    return str(floating_ip.floating_ip_address), 200

            networkID = vh.conn.network.find_network(network_id)
            if networkID is None:
                # self.logger.exception("Network " + network + " not found")
                return {"message":"Network not found"}, 400
            networkID = networkID.to_dict()["id"]
            floating_ip = vh.conn.network.create_ip(floating_network_id=networkID)
            floating_ip = vh.conn.network.get_ip(floating_ip)
            vh.conn.compute.add_floating_ip_to_server(
                server, floating_ip.floating_ip_address
            )
            return floating_ip, 201
        except Exception as e:
            return {"message": "Adding Floating IP to {0} with network {1} error:{2}".format(instance_id, network_id, e)}

class Network:
    def get(self, token, network_id):
        vh = VirtualMachineHandler(token)
        network = vh.conn.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200
    def list(self, token):
        vh = VirtualMachineHandler(token)
        network = vh.conn.network.networks()
        return [r for r in network], 200
