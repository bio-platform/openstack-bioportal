from VirtualMachineHandler import VirtualMachineHandler

class Metadata:
    def get(self, instance_id, token="token"):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        instance = vh.conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return vh.conn.compute.get_server_metadata(instance).to_dict(), 200

    def set(self, instance_id, metadata, token="token"):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        instance = vh.conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return vh.conn.compute.set_server_metadata(instance, **metadata)

    def delete(self, instance_id, keys_to_delete, token="token"):
        vh = VirtualMachineHandler("token", "clouds.yaml")
        instance = vh.conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = vh.conn.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in keys_to_delete:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        vh.conn.compute.delete_server_metadata(instance, keys_to_delete["keys"])
        return {}, 204