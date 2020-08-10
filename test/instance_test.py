import unittest

from Token import token

from app import app
from common.test.values import instance_id, project_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        print(self.login.headers)

        self.login = self.app.put("/", json={"project_id": project_id})
        print(self.login.headers)

    def test_get_success(self):
        response = self.app.get("/instances/%s/" % instance_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        print(response.json)
        assert response.status_code == 200 and response.json is not None

    def test_get_fail(self):
        response = self.app.get("/instances/invalid_id/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})

        assert response.status_code == 404


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_list_success(self):
        response = self.app.get("/instances/", headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.json is not None and response.status_code == 200
        print(response.json)


class TestPost(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        response = self.app.post("/instances/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"flavor": "standard.small",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "key1",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6",
                                       "metadata": {"medatadakey": "metadatavalue"}},
                                 )
        assert response.status_code == 201

    def test_failure_wrong_resource(self):
        response = self.app.post("/instances/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"flavor": "wrong_flavor",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "new_keypair",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        assert response.status_code == 400

    def test_failure_missing_argument(self):
        response = self.app.post("/instances/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"image": "cirros-0.4.0-x86_64",
                                       "key_name": "new_keypair",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        assert response.status_code == 400


class TestDelete(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        response = self.app.post("/instances/",
                                 headers={'Cookie': self.login.headers['Set-Cookie']},
                                 json={"flavor": "standard.small",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "key1",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6",
                                       "metadata": {"medatadakey": "metadatavalue"}},
                                 )
        if response.status_code == 201:
            instance_id = response.json["id"]
            from time import sleep
            while self.app.get("/instances/%s/" % instance_id,
                               headers={'Cookie': self.login.headers['Set-Cookie']}).json["status"] != "ACTIVE":
                sleep(5)
            response = self.app.delete("/instances/%s/" % instance_id,
                                       headers={'Cookie': self.login.headers['Set-Cookie']})
            assert response.status_code == 204


class TestUnloged(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_instance(self):
        response = self.app.get("/instances/%s/" % instance_id)
        assert response.status_code == 401 and response.json.get("message") is not None


if __name__ == '__main__':
    unittest.main()

