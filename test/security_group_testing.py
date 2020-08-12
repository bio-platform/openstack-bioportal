import unittest
from app import app
from Token import token
from common.test.values import security_group_id, project_id


class TestSecurityGroupGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        response = self.app.get("/security_groups/%s/" %security_group_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None


    def test_failure_group_not_found(self):
        response = self.app.get("/security_groups/sec_group/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 404 and \
               response.json == {}


class TestSecurityGroupList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        response = self.app.get("/security_groups/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None


class TestSecurityGroupCreate(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})


    def test_failure_missing_name(self):
        response = self.app.post("/security_groups/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and response.json is not None

    def test_failure_quota_exceeded(self):
        for i in range(10):
            response = self.app.post("/security_groups/",
                                     json={"name": "test_new_group" + str(i)},
                                     headers={'Cookie': self.login.headers['Set-Cookie']})
            assert response.status_code == 201 or response.status_code == 409
            if response.status_code == 409:
                break


class TestSecurityGroupDelete(unittest.TestCase):
    pass


class TestSecurityGroupRuleCreate(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})
        self.login = self.app.put("/", json={"project_id": project_id})

    def test_success(self):
        response = self.app.post("/security_groups/%s/security_group_rules/" %security_group_id,
                                 json={"type": "ssh"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None

    def test_failure_missing_type(self):
        response = self.app.post("/security_groups/%s/security_group_rules/" % security_group_id,
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and response.json is not None

    def test_failure_rules_exists(self):
        # TODO
        response = self.app.post("/security_groups/%s/security_group_rules/" % security_group_id,
                                 json={"type": "ssh"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None

        response = self.app.post("/security_groups/%s/security_group_rules/" % security_group_id,
                                 json={"type": "ssh"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 409 and "message" in response.json.keys()

    def test_failure_no_such_group(self):
        response = self.app.post("/security_groups/wrong_group/security_group_rules/",
                                 json={"type": "ssh"},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400
