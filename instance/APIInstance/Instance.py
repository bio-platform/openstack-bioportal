from flask_restful import Resource
from VirtualMachineHandler import VirtualMachineHandler


class Instance(Resource):

    def start_instance(self, input):
        vh = VirtualMachineHandler("token", "clouds.yaml",)
        return vh.start_server(**input)

    def stop_instace(self):
        pass

    def update_instance(self):
        pass

    def get_instance(self, instance_id):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        return vh.get_server(instance_id)

    def list_instances(self):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        return vh.list_servers()
