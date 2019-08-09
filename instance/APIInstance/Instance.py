from flask_restful import Resource
from VirtualMachineHandler import VirtualMachineHandler
from openstack.exceptions import ResourceNotFound

class Instance(Resource):

    def get(self,token, instance_id):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        server = vh.conn.compute.find_server(instance_id)
        if server is None:
            return {}, 404
        return server, 201

    def stop(self, token):
        return {}, 501

    def delete(self, token):
        return {}, 501

    def update(self, token):
        return {}, 501

    def list(self, token):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        tmp = vh.conn.compute.servers()
        return [r for r in tmp], 200

    def create(self,
               token,
               flavor,
               image,
               key_name,
               servername,
               network_id,
               diskspace=None,
               volume_name=None
               ):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403

            # metadata = {"elixir_id": elixir_id}
        image = vh.conn.compute.find_image(image)
        flavor = vh.conn.compute.find_flavor(flavor)
        network = vh.conn.network.find_network(network_id)
        key_pair = vh.conn.compute.find_keypair(key_name)
        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400
        server = vh.conn.compute.create_server(
                name=servername,
                image_id=image.id,
                flavor_id=flavor.id,
                networks=[{"uuid": network.id}],
                key_name=key_pair.name,
            )
        return server, 201
