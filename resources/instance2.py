"""
.. module:: instance2
.. moduleauthor:: Andrej Cermak <github.com/andrejcermak>
"""

import regex
from json import JSONDecoder as decoder
from flask import request
from flask_restful import Resource
from flask import session as flask_session

from .configuration import Configuration
from schema import StartTerraformSchema
from Connection import connect
import requests


class Instance2(Resource):
    @staticmethod
    def check_variables(config_name, input_variables, connection):

        conf, code= Configuration.get(config_name)
        if code == 404:
            return 1
        variables = []
        for _, var in conf["variables"].items():
            variables += var
        for variable_name in variables:
            if input_variables.get(variable_name) is None:
                return 1
        for key, value in input_variables.items():
            if key == "flavor":
                if connection.compute.find_flavor(value) is None:
                    return 1
            if key == "local_network_id":
                if connection.network.find_network(value) is None:
                     return 1
            if key == "ssh":
                if connection.compute.find_keypair(value) is None:
                    return 1
        return 0



    @staticmethod
    def post():
        """
            **Create new instance using terraform and terrestrial**

            This function allows users to start new instance from configurations at
            https://github.com/bio-platform/bioportal_configs.

            Its json input is specified by schema.StartTerraformSchema

            :return: terraform task id

            - Example::

                  curl -X POST bio-portal.metacentrum.cz/api/instancesv2/ -H 'Cookie: cookie from scope' -H
                  'content-type: application/json' --data json specified in schema

            - Expected Success Response::

                HTTP Status Code: 201

                json-format: {"id": task_id}

            - Expected Fail Response::

                HTTP Status Code: 400

                {"message": "resoucre not found"}


        """
        connection = connect(flask_session['token'], flask_session['project_id'])
        data = StartTerraformSchema().load(request.json)
        data["input_variables"]["token"] = connection.authorize()
        #if Instance2.check_variables(data["name"], data["input_variables"], connection):
        #    return {"message": "resource not found"}, 400
        response = requests.post("http://terrestrial_api_1:8000/api/v1/configurations/%s/apply?async"
                                 % data["name"],
                                 headers={'Authorization': 'Token dev'},
                                 data=data["input_variables"])
        return {"id": response.content.decode()}, response.status_code


class Task(Resource):

    @staticmethod
    def get(task_id):
        """
            **Get state of specific task**

            This function allows users to get task state its ID.

            :param task_id: id of the terraform task from terrestrial
            :type task_id: id from terrestrial
            :return: task state and eventually error message and logs

            - Example::

                curl -X GET bio-portal.metacentrum.cz/api/tasks/_task_id/
                 -H 'Cookie: cookie from scope' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format:

                {"state": "PENDING", "reason": {}, "log": ""}

                or

                HTTP Status Code: 200

                {"state": "STARTED", "reason": {}, "log": ""}

                or

                HTTP Status Code: 201

                {"state": "STARTED", "reason": {}, "log": terraform logs}

            - Expected Fail Response::

                HTTP Status Code: 201

                {"state": "ERROR, "reason": reason why task failed}


        """
        connect(flask_session['token'], flask_session['project_id'])
        response = requests.get("http://terrestrial_api_1:8000/api/v1/tasks/" + task_id,
                                headers={'Authorization': 'Token dev'})
        state = response.content.decode()

        if state == "PENDING" or state == "STARTED":
            return {"state": state, "reason": {}, "log": ""}, 200
        if state == "SUCCESS":
            result = requests.get("http://terrestrial_api_1:8000/api/v1/tasks/%s/result" % task_id,
                                  headers={'Authorization': 'Token dev'}).content.decode()
            if result.find("Apply complete!") != -1:
                return {"state": state, "reason": {}, "log": result}, 201

            if result.find("Error creating OpenStack") != -1:
                pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
                print("reason", result)
                reason, _ = decoder().raw_decode(pattern.findall(result)[0])
                keys = [i for i in reason.keys()]
                return {"state": "ERROR", "reason": reason[keys[0]], "log": result}, 201

        return {"state": state, "reason": {}, "log": ""}, 200
