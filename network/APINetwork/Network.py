from requests import put
from Connection import connect
from flask import session


class Gateway:

    def add(self, router_id, external_network):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401
        router = conn.network.find_router(router_id)
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
                   headers={"X-Auth-Token": conn.authorize()}, json=router_gateway_request).json()


class FloatingIp:

    def create(self, instance_id, network_id):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401
        try:
            server = conn.compute.find_server(instance_id)
            if server is None:
                return {"message": "Server not found"}, 400

            for values in server.addresses.values():
                for address in values:
                    if address["OS-EXT-IPS:type"] == "floating":
                        return address["addr"], 200

            for floating_ip in conn.network.ips():
                if not floating_ip.fixed_ip_address:
                    conn.compute.add_floating_ip_to_server(
                        server, floating_ip.floating_ip_address
                    )

                    return str(floating_ip.floating_ip_address), 200

            networkID = conn.network.find_network(network_id)
            if networkID is None:

                return {"message":"Network not found"}, 400
            networkID = networkID.to_dict()["id"]
            floating_ip = conn.network.create_ip(floating_network_id=networkID)
            floating_ip = conn.network.get_ip(floating_ip)
            conn.compute.add_floating_ip_to_server(
                server, floating_ip.floating_ip_address
            )
            return floating_ip, 201
        except Exception as e:
            return {"message": "Adding Floating IP to {0} with network {1} error:{2}".format(instance_id, network_id, e)}


class Network:
    def get(self, network_id):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        network = conn.network.find_network(network_id)
        if network is None:
            return {}, 404
        return network.to_dict(), 200

    def list(self):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        network = conn.network.networks()
        return [r for r in network], 200
