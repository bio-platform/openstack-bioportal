"""
.. module:: instance2
.. moduleauthor:: Andrej Cermak <github.com/andrejcermak>
"""

import base64

from oslo_utils import encodeutils

from flask import request
from flask_restful import Resource
from flask import session as flask_session

from schema import StartServerSchema
from Connection import connect
import requests

from python_terraform import Terraform
import regex

class Instance2(Resource):

    @staticmethod
    def post():
        connection = connect(flask_session['token'], flask_session['project_id'])
        data = StartServerSchema().load(request.json)

        image = connection.compute.find_image(data["image"])
        flavor = connection.compute.find_flavor(data["flavor"])
        network = connection.network.find_network(data["network_id"])
        key_pair = connection.compute.find_keypair(data["key_name"])

        req = requests.get(
            "https://raw.githubusercontent.com/bio-platform/bio-class/master/install/cloud-init-bioconductor-image.sh")
        text = encodeutils.safe_encode(req.text.encode("utf-8"))
        init_script = base64.b64encode(text).decode("utf-8")

        if (image is None) or (flavor is None) or (network is None) or (key_pair is None):
            return {"message": "resource not found"}, 400

        from app import app

        user_variables = {
            "instance_name": "data",
            "key_pair": key_pair.name,
            "network_id": network.id,
            "user_name": data["metadata"]["name"],
            "user_email": data["metadata"]["email"],
            "floating_ip": "78.128.250.94",
            "init_script": init_script
        }
        response = requests.post("http://127.0.0.1:5000/api/v1/configurations/with_vars/apply?async",
                             headers={'Authorization': 'Token token'},
                             data=user_variables)
        print("api:", response.status_code, type(response.status_code))
        return {"id": response.content.decode()}, response.status_code

class Instance2Task(Resource):
    @staticmethod
    def get(task_id):
        print("aa", task_id)
        connection = connect(flask_session['token'], flask_session['project_id'])
        response = requests.get("http://127.0.0.1:5000/api/v1/tasks/"+task_id,
                                 headers={'Authorization': 'Token token'})
        return response.content, response.status_code