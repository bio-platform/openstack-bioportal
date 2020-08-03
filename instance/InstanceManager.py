from flask import request
from flask_restful import Resource

import DefaultManager
from instance.Instance import Instance
from instance.InstanceSchema import StartServerSchema


class InstanceManager(Resource):
    """
            **Get List of Teachers**

            :return: teacher's information in json and http status code

            - Example::

                  curl -X GET http://localhost:5000/ -H 'cache-control: no-cache' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200
                {
                    "Teachers": [
                        {
                            "id": 1,
                            "name": "Jane Vargas",
                            "subject": "Science"
                        },
                        {
                            "id": 2,
                            "name": "John Doe",
                            "subject": "Math"
                        },
                        {
                            "id": 3,
                            "name": "Jenny Lisa",
                            "subject": "English"
                        }
                    ]
                }
            """
    @staticmethod
    def post():
        return DefaultManager.manage(Instance().create, request.json, StartServerSchema)

    @staticmethod
    def get(instance_id=None):
        if instance_id is None:
            return DefaultManager.manage(Instance().list, request.json)
        else:
            return DefaultManager.manage(Instance().get, request.json, instance_id=instance_id)

    @staticmethod
    def put():
        return DefaultManager.manage(Instance().update, request.json)

    @staticmethod
    def delete(instance_id):
        return DefaultManager.manage(Instance().delete, request.json, instance_id=instance_id)
