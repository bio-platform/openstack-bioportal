import unittest

from app import app
# from balast.Token import token
from common.test.values import network_id, router_id, external_network_id

token = "eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVkdV9wZXJzb25fZW50aXRsZW1lbnRzIGVtYWlsIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY3NDM0Nzc4LCJpYXQiOjE1Njc0MzExNzgsImp0aSI6Ijg5OWQyNTljLWM1YzgtNGE4Yi1iODdiLTM3MGExYzc4ZWQ2MCJ9.eAd0NqHgtSg_J4Rge6PXTQ02q8vuc94fpyGvlqS8XcBSux_ARstIFiXs1M_O6Hgry9d07KbJ4cWN1BljmAAegLsv8jnmt9cMTLvHPaxGbRFI9b2-xREyjTDlBQNx698Qs4fXZ-g99-T3M6FRCPU5-t00Kj73pOmtofVF0HciR7k0Vr01kHkw0uO__SB82qjus7afBoVvOQ_49hU2sRTMT1Lu7VvzxwP9i40hpWh12zFYFF7zYD448B5YnthcoHEUXo5GuYb2s0a1zvg__lttnjP6VEM1yG-Afc4fyCw_kYKhh9mlDqoX2HXsp0_AS62d92Mf0bNCnTkm2PVEsWwGVA"


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
        response = self.app.get("/networks/%s/" % network_id,
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
        response = self.app.put("/gateways/%s/" % router_id,
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


class TestRoutersList(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.login = self.app.post("/", json={"token": token})

    def test_success(self):
        response = self.app.get("/routers/",
                                headers={'Cookie': self.login.headers['Set-Cookie']})
        print(response.json)
        assert response.status_code == 200 and response.json is not None

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
