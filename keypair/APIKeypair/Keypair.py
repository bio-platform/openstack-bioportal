from flask_restful import Resource
from VirtualMachineHandler import VirtualMachineHandler


class Keypair(Resource):

    def create_keypair(self, input):
        vh = VirtualMachineHandler("token", "clouds.yaml",)
        return vh.import_keypair(**input)

    def update_keypair(self):
        pass

    def get_keypair(self, keypair_id):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        return vh.get_keypair(keypair_id)

    def list_keypairs(self):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        return vh.list_keypairs()
