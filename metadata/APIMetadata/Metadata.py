from Connection import connect
from flask import session


class Metadata:
    def get(self, instance_id):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        instance = conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        return conn.compute.get_server_metadata(instance).to_dict(), 200

    def set(self, instance_id, metadata):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401
        instance = conn.compute.find_server(instance_id)

        if instance is None:
            return {"message": "instance not found"}, 400
        return conn.compute.set_server_metadata(instance, **metadata)

    def delete(self, instance_id, keys):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401
        instance = conn.compute.find_server(instance_id)
        if instance is None:
            return {"message": "instance not found"}, 400
        metadata = conn.compute.get_server_metadata(instance).to_dict()["metadata"]
        for key in keys:
            if metadata.get(key) is None:
                return {"message": "key not in metadata"}, 400

        conn.compute.delete_server_metadata(instance, keys)
        return {}, 204
