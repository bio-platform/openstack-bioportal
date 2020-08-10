import unittest
from Token import token
from app import app


class TestLogin(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_success(self):
        response= self.app.post("/", json={"token": token})
        assert response.status_code == 200 and response.json is not None

    def test_login_fail(self):
        response = self.app.post("/", json={"token": "wrong token"})
        assert response.status_code == 401


class TestScope(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token}).headers
        self.project_id = self.app.get("/projects/").json["projects"][0]["id"]

    def test_scope_success(self):
        response = self.app.put("/", json={"project_id": self.project_id})
        assert response.status_code == 204

    def test_scope_fail(self):
        response = self.app.put("/", json={"project_id": "wrong project"})
        assert response.status_code == 400


class TestVerification(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token}).headers
        self.project_id = self.app.get("/projects/").json["projects"][0]["id"]
        self.app.put("/", json={"project_id": self.project_id})

    def test_get_success(self):
        response = self.app.get("/")
        assert response.status_code == 200

    def test_get_fail(self):
        pass
        #TODO ako testovat takyto pripad hmmmm
        # with self.app as client:
        #     with client.session_transaction() as sess:
        #         # Modify the session in this context block.
        #         sess["project_id"] = "project_id"
        #         sess["token"] = "8"
        #     response = client.get("/")
        #     print(response)
        #     assert response.status_code == 401
        #

if __name__ == '__main__':
    unittest.main()
