from flask_restful import Resource
from oslo_utils import encodeutils
import base64


class Instance(Resource):

    def get(self,connection, instance_id):

        server = connection.compute.find_server(instance_id)
        if server is None:
            return {}, 404
        return server, 201

    def stop(self):
        return {}, 501

    def delete(self):
        return {}, 501

    def update(self):
        return {}, 501

    def list(self, connection):

        tmp = connection.compute.servers()
        return [r for r in tmp], 200

    def create(self,
               connection,
               flavor,
               image,
               key_name,
               servername,
               network_id,
               metadata,
               diskspace=None,
               volume_name=None
               ):

        image = connection.compute.find_image(image)
        flavor = connection.compute.find_flavor(flavor)
        network = connection.network.find_network(network_id)
        key_pair = connection.compute.find_keypair(key_name)

        with open("cloud-init-bioconductor-image.sh", "r") as file:
            text = file.read()
            text = encodeutils.safe_encode(text.encode("utf-8"))
        init_script = base64.b64encode(text).decode("utf-8")

        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400
        server = connection.compute.create_server(
                name=servername,
                image_id=image.id,
                flavor_id=flavor.id,
                networks=[{"uuid": network.id}],
                key_name=key_pair.name,
                metadata=metadata,
                user_data=init_script
            )
        return server, 201
