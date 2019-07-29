from flask_restful import Resource
from VirtualMachineHandler import VirtualMachineHandler


class SecurityGroup(Resource):
    vh = VirtualMachineHandler("token", "clouds.yaml")

    def create(self, name):
        new_security_group = self.vh.conn.network.create_security_group(name=name)
        return new_security_group

    def get(self, security_group_id):
        security_group = self.conn.network.find_security_group(security_group_id)
        if security_group is None:
            return {}, 404
        return security_group, 200

    def list(self):
        tmp = self.list_default(self.conn.network.networks())
        return [r for r in tmp], 200

class SecurityGroupRule(Resource):
    vh = VirtualMachineHandler("token", "clouds.yaml")
    def create(self, type, security_group_id):
        if type == "ssh":
            self.vh.conn.network.create_security_group_rule(
                direction="ingress",
                protocol="tcp",
                port_range_max=22,
                port_range_min=22,
                security_group_id=security_group_id,
                ether_type="IPv4",

            )
        if type == "all_icmp":
            self.vh.conn.network.create_security_group_rule(
                direction="ingress",
                protocol="ICMP",
                security_group_id=security_group_id,
                ether_type="IPv4",
                remote_ip_prefix= "0.0.0.0/0")
        return new_security_group, 201