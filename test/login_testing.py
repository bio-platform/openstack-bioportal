import unittest

from Token import token
from app import app
from common.test.values import instance_id

import json
class TestLogin(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_success(self):
        self.login = self.app.post("/", json={"token": token})
        print("headers", self.login.headers)
        print(dir(self.login.headers))
        #assert response.status_code == 200 and response.json is not None

    def test_login_fail(self):
        response = self.app.post("/", json={"token": "wrong token"})




if __name__ == '__main__':
    unittest.main()
