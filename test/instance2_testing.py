import unittest

from Token import token

from app import app
from common.test.values import instance_id, project_id

import requests

class TestPost(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})
        print(self.login.headers)

    def test_success(self):
        response = self.app.post("/instancesv2/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"flavor": "standard.2core-16ram",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "zenbook mint",
                                       "servername": "new_server_1",
                                       "network_id": "03b21c24-910f-4ec5-a8f3-419db219b383",
                                       "metadata": {"name": "xcermak5",
                                                    "email": "email@"}})
        print(response.json.get("id"))
        assert response.status_code == 201
        assert response.json.get("id") is not None

class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        task_id = "c33d93df-cc79-4cee-81d9-2d6964348003"
        response = self.app.get("/instancesv2/tasks/"+task_id,
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 )
        print(response.json, response.status_code)
        assert response.status_code == 201
        assert response.json.get("id") is not None

class TestUnloged(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_instance(self):
        response = self.app.get("/instances/%s/" % instance_id)
        assert response.status_code == 401 and response.json.get("message") is not None


if __name__ == '__main__':
    unittest.main()

