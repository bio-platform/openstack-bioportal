import unittest

from Token import token

from app import app
from common.test.values import keypair_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_get_success(self):
        response = self.app.get("/keypairs/%s/" % keypair_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/keypairs/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None


class TestPost(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success_created(self):
        response = self.app.post("/keypairs/",
                                 json={
                                     "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ andrej",
                                     "keyname": "unused_name"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None

    def test_success_exists(self):
        response = self.app.post("/keypairs/",
                                 json={
                                     "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ andrej",
                                     "keyname": "cba"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None

    def test_failure_invalid_key(self):
        response = self.app.post("/keypairs/",
                                 json={"public_key": "abc",
                                       "keyname": "cba"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and response.json is not None


class TestPut(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_put_not_implemented(self):
        response = self.app.put("/keypairs/%s/" % keypair_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 501 and not response.json


class TestDelete(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_put_not_implemented(self):
        response = self.app.delete("/keypairs/%s/" % keypair_id,
                                   headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 501 and not response.json


if __name__ == '__main__':
    unittest.main()
