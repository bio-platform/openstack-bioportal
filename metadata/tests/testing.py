import unittest
from app import app
from Token import token
from common.test.values import instance_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get("/metadata/%s/" %instance_id,
                                json={"token": token})
        assert response.status_code == 200 and response.json is not None
        assert "metadata" in response.json.keys()

    def test_failure_wrong_token(self):
        response = self.app.get("/metadata/%s/" %instance_id,
                                json={"token": "wrong token"})
        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.get("/metadata/%s/" %instance_id,
                                json={})
        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_instance_not_found(self):
        response = self.app.get("/metadata/%s/" % "invalid_instance_id",
                                json={"token": token})
        print(response.json)
        assert response.status_code == 400 and \
               "message" in response.json.keys()


class TestSet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"token": token,
                                      "metadata": {"test_metadata_key":
                                                   "test_metadata_value"}})
        assert response.status_code == 200 and response.json is not None
        assert "metadata" in response.json.keys() and response.json["metadata"]["test_metadata_key"] == "test_metadata_value"

    def test_failure_wrong_token(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"token": "wrong token",
                                      "metadata": {"test_metadata_key":
                                                       "test_metadata_value"}})

        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"metadata": {"test_metadata_key":
                                                   "test_metadata_value"}})
        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_missing_metadata(self):
        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"token": token})
        assert response.status_code == 400 and response.json is not None

    def test_failure_instance_not_found(self):
        response = self.app.put("/metadata/%s/" % "invalid_instance_id",
                                json={"token": token})
        assert response.status_code == 400 and \
               "message" in response.json.keys()


class TestDelete(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):

        response = self.app.put("/metadata/%s/" % instance_id,
                                json={"token": token,
                                      "metadata": {"test_metadata_key":
                                                       "test_metadata_value"}})
        assert response.status_code == 200

        response = self.app.delete("/metadata/%s/" % instance_id,
                                json={"token": token,
                                      "keys": ["test_metadata_key"]})
        assert response.status_code == 204

    def test_failure_wrong_token(self):
        response = self.app.delete("/metadata/%s/" % instance_id,
                                json={"token": "wrong token",
                                      "keys": ["test_metadata_key"]})

        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.delete("/metadata/%s/" % instance_id,
                                   json={"keys": ["test_metadata_key"]})
        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_instance_not_found(self):
        response = self.app.delete("/metadata/%s/" % "invalid_instance_id",
                                   json={"token": token,
                                         "keys": ["test_metadata_key"]})
        assert response.status_code == 400 and \
               "message" in response.json.keys()
