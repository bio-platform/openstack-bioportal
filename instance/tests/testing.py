import unittest
from app import app
from Token import token

class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_post(self):
        pass
    def test_get_success(self):
        response = self.app.get("/instances/", json=dict(token=token))
        assert response.json is not None and response.status_code == 200

    def test_get_failure_missing_token(self):
        response = self.app.get("/instances/", json={})
        assert response.status_code == 400

    def test_get_failure_wrong_token(self):
        response = self.app.get("/instances/", json=dict(token="wrong token"))
        assert response.status_code == 403
if __name__ == '__main__':
    unittest.main()
