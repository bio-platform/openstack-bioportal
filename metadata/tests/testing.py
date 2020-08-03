import unittest

from Token import token

from app import app
from common.test.values import instance_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/metadata/%s/" % instance_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None
        assert "metadata" in response.json.keys()

    def test_failure_instance_not_found(self):
        response = self.app.get("/metadata/%s/" % "invalid_instance_id",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        print(response.json)
        assert response.status_code == 400 and \
               "message" in response.json.keys()


class TestSet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"metadata": {"test_metadata_key":
                                                       "test_metadata_value"}},
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None
        assert "metadata" in response.json.keys() and response.json["metadata"][
            "test_metadata_key"] == "test_metadata_value"

    def test_failure_missing_metadata(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and response.json is not None

    def test_failure_instance_not_found(self):
        response = self.app.put("/metadata/%s/" % "invalid_instance_id",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and \
               "message" in response.json.keys()


class TestDelete(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"metadata": {"test_metadata_key":
                                                       "test_metadata_value"}},
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200

        response = self.app.delete("/metadata/%s/" % instance_id,
                                   json={"keys": ["test_metadata_key"]},
                                   headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 204

    def test_failure_instance_not_found(self):
        response = self.app.delete("/metadata/%s/" % "invalid_instance_id",
                                   json={"keys": ["test_metadata_key"]},
                                   headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and \
               "message" in response.json.keys()
