import unittest
from Token import token
from app import app


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": "746105e4689f4cdaa621eecf9a86818f"})

    def test_success(self):
        response = self.app.get("/limits/", headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None
        assert "ram" in response.json.keys()
