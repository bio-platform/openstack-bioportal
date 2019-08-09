import unittest
from app import app
from Token import token
from common.test.values import instance_id

class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_success(self):
        response = self.app.get("/instances/%s/" % instance_id,
                                json={"token": token})
        assert response.status_code == 201 and response.json is not None

    def test_get_failure_wrong_token(self):
        response = self.app.get("/instances/%s/" % instance_id,
                                json={"token":"wrong token"})
        assert response.status_code == 403

    def test_get_failure_not_found(self):
        response = self.app.get("/instances/%s/" % "invalid_instance_id",
                                json=dict(token=token))

        assert (not response.json) and (response.status_code == 404)

class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_list_success(self):
        response = self.app.get("/instances/", json=dict(token=token))
        assert response.json is not None and response.status_code == 200

    def test_list_failure_missing_token(self):
        response = self.app.get("/instances/", json={})
        assert response.status_code == 400

    def test_list_failure_wrong_token(self):
        response = self.app.get("/instances/", json=dict(token="wrong token"))
        assert response.status_code == 403


class TestPost(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.post("/instances/",
                                 json={"token": token,
                                       "flavor": "standard.small",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "key1",
                                       "servername": "new_server_1",
                                        "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        print(response.status_code, response.json)
        print()
        assert response.status_code == 201

    def test_failure_wrong_resource(self):
        response = self.app.post("/instances/",
                                 json={"token": token,
                                       "flavor": "wrong_flavor",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "new_keypair",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        assert response.status_code == 400

    def test_failure_wrong_token(self):
        response = self.app.post("/instances/",
                                 json={"token": "token",
                                       "flavor": "standard.small",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "key1",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        assert response.status_code == 403

    def test_failure_missing_argument(self):
        response = self.app.post("/instances/",
                                 json={"token": "token",
                                       "image": "cirros-0.4.0-x86_64",
                                       "key_name": "new_keypair",
                                       "servername": "new_server_1",
                                       "network_id": "1fd8ee12-75fa-40d1-b218-8278e22fd3b6"})
        assert response.status_code == 400
if __name__ == '__main__':
    unittest.main()
