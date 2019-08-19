from flask_restful import Resource
from Connection import connect
from flask import session


class Instance(Resource):

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

        server = conn.compute.find_server(instance_id)
        if server is None:
            return {}, 404
        return server, 201

    def stop(self):
        return {}, 501

    def delete(self):
        return {}, 501

    def update(self):
        return {}, 501

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
        tmp = conn.compute.servers()
        return [r for r in tmp], 200

    def create(self,
               flavor,
               image,
               key_name,
               servername,
               network_id,
               diskspace=None,
               volume_name=None
               ):
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            conn = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        image = conn.compute.find_image(image)
        flavor = conn.compute.find_flavor(flavor)
        network = conn.network.find_network(network_id)
        key_pair = conn.compute.find_keypair(key_name)
        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400
        server = conn.compute.create_server(
                name=servername,
                image_id=image.id,
                flavor_id=flavor.id,
                networks=[{"uuid": network.id}],
                key_name=key_pair.name,
            )
        return server, 201
