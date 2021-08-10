import requests
from flask_restful import Resource
from Connection import connect
from flask import session
from .configuration import Configuration

class Instruction(Resource):

    @staticmethod
    def get(instance_id):
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
        INSTRUCTIONS = "instructions"
        connection = connect(session['token'], session['project_id'])
        if instance_id is None:
            return {}, 404

        server = connection.compute.find_server(instance_id)
        if server is None:
            return {}, 404
        meta = server.metadata
        if meta.get(INSTRUCTIONS) is None:
            return {}, 404
        conf = Configuration.get(meta.get(INSTRUCTIONS))
        return {"instructions": conf[0][INSTRUCTIONS]}, 200
