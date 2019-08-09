import unittest
from app import app
from Token import token
from common.test.values import network_id, router_id, external_network_id, instance_id


class TestNetworkList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get("/networks/",
                                json={"token": token})

        assert response.status_code == 200 and response.json is not None

    def test_failure_wrong_token(self):
        response = self.app.get("/networks/",
                                json={"token": "wrong token"})
        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.get("/networks/",
                                json={})
        assert response.status_code == 400 and \
               "message" in response.json.keys()


class TestNetworkGet(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get("/networks/%s/" %network_id,
                                json={"token": token})
        print(response.json, response.status_code)
        assert response.status_code == 200 and response.json is not None

    def test_failure_wrong_token(self):
        response = self.app.get("/networks/%s/" %network_id,
                                json={"token": "wrong token"})
        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.get("/networks/%s/" %network_id,
                                json={})
        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_group_not_found(self):
        response = self.app.get("/networks/network/",
                                json={"token": token})
        assert response.status_code == 404 and \
               response.json == {}


class TestGatewayPut(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_success(self):
        response = self.app.put("/gateways/%s/" %router_id,
                                json={"token": token,
                                      "external_network": external_network_id})

        assert response.status_code == 200 and response.json is not None

    def test_failure_wrong_token(self):
        response = self.app.put("/gateways/%s/" %router_id,
                                json={"token": "wrong token",
                                      "external_network": external_network_id})

        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.put("/gateways/%s/" %router_id,
                                json={"external_network": external_network_id})

        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_router_not_found(self):
        response = self.app.put("/gateways/%s/" % "router",
                                json={"token": token,
                                      "external_network": external_network_id})
        assert response.status_code == 400 and "message" in response.json.keys()


class TestFloatingIpPost(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_failure_wrong_token(self):
        response = self.app.post("/floating_ips/",
                                 json={"token": "token",
                                       "instance_id": instance_id,
                                       "network_id": external_network_id})

        assert response.status_code == 403 and \
               "message" in response.json.keys()

    def test_failure_missing_token(self):
        response = self.app.post("/floating_ips/",
                                 json={"instance_id": instance_id,
                                       "network_id": external_network_id})

        assert response.status_code == 400 and \
               "message" in response.json.keys()

    def test_failure_instance_not_found(self):
        response = self.app.post("/floating_ips/",
                                json={"token": token,
                                      "instance_id": "instance_id",
                                      "network_id": external_network_id})

        assert response.status_code == 400 and "message" in response.json.keys()

    # TODO
    def test_success_created(self):
        response = self.app.post("/floating_ips/",
                                 json={"token": token,
                                       "instance_id": instance_id,
                                       "network_id": external_network_id})

        assert response.status_code == 201 and response.json is not None

    def test_success_floating_ip_exists_is_not_associated(self):
        pass

    def test_success_server_has_floating_ip(self):
        pass
