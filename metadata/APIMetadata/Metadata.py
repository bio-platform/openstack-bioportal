from VirtualMachineHandler import VirtualMachineHandler

class Metadata:
    def get(self, token, instance_id):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        instance = vh.conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return vh.conn.compute.get_server_metadata(instance).to_dict(), 200

    def set(self, token, instance_id, metadata):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        instance = vh.conn.compute.find_server(instance_id)

        if instance is None:
            return {"message": "instance not found"}, 400
        return vh.conn.compute.set_server_metadata(instance, **metadata)

    def delete(self, token, instance_id, keys):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        instance = vh.conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = vh.conn.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in keys:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        vh.conn.compute.delete_server_metadata(instance, keys)
        return {}, 204
