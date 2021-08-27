import unittest

from Token import token

from app import app
from common.test.values import instance_id, project_id


class TestPost(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})
        print(self.login.headers)

    def test_success(self):
        print("aa")
        response = self.app.post("/instancesv2/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"name": "bioconductor",
                                       "input_variables": {
                                           "flavor": "standard.2core-16ram",
                                           "ssh": "zenbook mint",
                                           "instance_name": "new_server_1",
                                           "local_network_id": "03b21c24-910f-4ec5-a8f3-419db219b383",
                                           "floating_ip": "78.128.250.94",
                                           "user_name": "xcermak5",
                                           "user_email": "485555@muni.cz"
                                        }})

        print(response.json.get("id"))
        print(response)
        assert response.status_code == 201
        assert response.json.get("id") is not None

class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        task_id = "a72755ca-b60a-49f3-be76-a0f4436d5e60"
        response = self.app.get("/tasks/%s/" %task_id,
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

