import unittest
from app import app
from Token import token


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/projects/")
        assert response.status_code == 200 and response.json is not None
