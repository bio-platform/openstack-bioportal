import unittest
from app import app
from Token import token
from common.test.values import network_id, router_id, external_network_id, instance_id


class TestNetworkList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/networks/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})

        assert response.status_code == 200 and response.json is not None


class TestNetworkGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/networks/%s/" %network_id,
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None


    def test_failure_group_not_found(self):
        response = self.app.get("/networks/network/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 404 and \
               response.json == {}


class TestGatewayPut(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.put("/gateways/%s/" %router_id,
                                json={"external_network": external_network_id},
                                headers={'Cookie': self.login.headers['Set-Cookie']})

        assert response.status_code == 200 and response.json is not None

    def test_failure_router_not_found(self):
        response = self.app.put("/gateways/%s/" % "router",
                                json={"external_network": external_network_id},
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 400 and "message" in response.json.keys()


# TODO
class TestFloatingIpPost(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_failure_instance_not_found(self):
        response = self.app.post("/floating_ips/",
                                json={"instance_id": "instance_id",
                                      "network_id": external_network_id},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})

        assert response.status_code == 400 and "message" in response.json.keys()

    """
    def test_success_created(self):
        response = self.app.post("/floating_ips/",
                                 json={"instance_id": instance_id,
                                       "network_id": external_network_id},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None

    def test_success_floating_ip_exists_is_not_associated(self):
        response = self.app.post("/floating_ips/",
                                 json={"instance_id": instance_id,
                                       "network_id": external_network_id},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 201 and response.json is not None

    def test_success_server_has_floating_ip(self):
        response = self.app.post("/floating_ips/",
                                 json={"instance_id": instance_id,
                                       "network_id": external_network_id},
                                 headers={'Cookie': self.login.headers['Set-Cookie']})
        assert response.status_code == 200 and response.json is not None
    """