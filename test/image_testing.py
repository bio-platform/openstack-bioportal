import unittest

from Token import token

from app import app
from common.test.values import image_id, project_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_get_success(self):
        response = self.app.get("/images/%s/" % image_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None

    def test_get_fail(self):
        response = self.app.get("/images/invalid_id/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 404

class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_list_success(self):
        response = self.app.get("/images/", headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.json is not None and response.status_code == 200
