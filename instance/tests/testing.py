import unittest
from app import app
from Token import token
from common.test.values import instance_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_get_success(self):
        response = self.app.get("/instances/%s/" % instance_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_list_success(self):
        response = self.app.get("/instances/", headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.json is not None and response.status_code == 200
        print(response.json)

class TestPost(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

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


if __name__ == '__main__':
    unittest.main()
