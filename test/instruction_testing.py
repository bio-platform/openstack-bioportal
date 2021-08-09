import unittest
from Token import token
from app import app
from common.test.values import project_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_get_success(self):
        instance_id = "5da748bb-e9e1-4daf-a3c8-a5600a56f6b8"
        response = self.app.get("/instructions/%s/" % instance_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        print(response.json)
        # assert response.status_code == 200 and response.json is not None