from flask_restful import Resource
from VirtualMachineHandler import VirtualMachineHandler
from openstack.exceptions import ResourceNotFound

class Instance(Resource):

    def get(self, openstack_id, token):
        vh = VirtualMachineHandler("token", "clouds.yaml",)
        server = vh.conn.compute.find_server(openstack_id)
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
        vh = VirtualMachineHandler(token, "clouds.yaml")
        tmp = vh.conn.compute.servers()
        return [r for r in tmp], 200

    def create(self,
               token,
               flavor,
               image,
               key_name,
               servername,
               network,
               diskspace=None,
               volume_name=None
               ):
        vh = VirtualMachineHandler(token, "clouds.yaml")
        try:
            # metadata = {"elixir_id": elixir_id}
            image = vh.conn.compute.get_image(image=image)
            flavor = vh.conn.compute.get_flavor(flavor=flavor)
            network = vh.conn.network.get_network(network=network)
            key_pair = vh.conn.compute.get_keypair(keypair=key_name)

            server = self.conn.compute.create_server(
                name=servername,
                image_id=image.id,
                flavor_id=flavor.id,
                networks=[{"uuid": network.id}],
                key_name=key_pair.name,
            )
            return server, 201
        except ResourceNotFound as e:
            print(e)
            return {"message": str(e)}, 400
