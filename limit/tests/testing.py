import unittest
from app import app
from Token import token


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get("/limits/",
                                json={"token": token})
        assert response.status_code == 200 and response.json is not None
        assert "ram" in response.json.keys()

    def test_failure_wrong_token(self):
        response = self.app.get("/limits/",
                                json={"token": "wrong token"})
        assert response.status_code == 403 and\
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.get("/limits/",
                                json={})
        assert response.status_code == 400 and \
               "message" in response.json.keys()