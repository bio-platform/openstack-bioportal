class Metadata:
    def get(self, connection, instance_id):

        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.get_server_metadata(instance).to_dict(), 200

    def set(self, connection, instance_id, metadata):
        instance = connection.compute.find_server(instance_id)

        if instance is None:
            return {"message": "instance not found"}, 400
        return connection.compute.set_server_metadata(instance, **metadata)

    def delete(self, connection, instance_id, keys):

        instance = connection.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = connection.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in keys:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        connection.compute.delete_server_metadata(instance, keys)
        return {}, 204
