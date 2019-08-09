import unittest
from app import app
from Token import token
from common.test.values import keypair_id


class TestGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_success(self):
        response = self.app.get("/keypairs/%s/" % keypair_id,
                                json={"token": token})
        assert response.status_code == 200 and response.json is not None
    def test_failure_wrong_token(self):
        response = self.app.get("/keypairs/%s/" % keypair_id,
                                json={"token":"wrong token"})
        assert response.status_code == 403

    def test_failure_missing_token(self):
        response = self.app.get("/keypairs/%s/" % keypair_id,
                                json={})
        assert response.status_code == 400


class TestList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get("/keypairs/",
                                json={"token": token})
        assert response.status_code == 200 and response.json is not None

    def test_get_failure_wrong_token(self):
        response = self.app.get("/keypairs/",
                                json={"token":"wrong token"})
        assert response.status_code == 403

    def test_list_failure_missing_token(self):
        response = self.app.get("/keypairs/", json={})
        assert response.status_code == 400


class TestPost(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success_created(self):
        response = self.app.post("/keypairs/",
                                json={"token": token,
                                      "public_key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ andrej",
                                      "keyname":"cba"})
        assert response.status_code == 201 and response.json is not None

    def test_success_exists(self):
        response = self.app.post("/keypairs/",
                                 json={"token": token,
                                       "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ andrej",
                                       "keyname": "cba"})
        assert response.status_code == 200 and response.json is not None

    def test_failure_invalid_key(self):
        response = self.app.post("/keypairs/",
                                json={"token": token,
                                      "public_key":"abc",
                                      "keyname":"cba"})
        assert response.status_code == 400 and response.json is not None
