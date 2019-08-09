from VirtualMachineHandler import VirtualMachineHandler


class SecurityGroup:

    def create(self, token, name):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        try:
            new_security_group = vh.conn.network.create_security_group(name=name)
            return new_security_group, 201
        except Exception as e:
            return {"message": str(e)}, 409

    def get(self, token, security_group_id):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        security_group = vh.conn.network.find_security_group(security_group_id)
        if security_group is None:
            return {}, 404
        return security_group.to_dict(), 200

    def list(self, token):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        tmp = vh.conn.network.security_groups()
        return [r for r in tmp], 200

    def update(self):
        return {}, 501

    def delete(self):
        return {}, 501

class SecurityGroupRule:

    def create(self, token, security_group_id, type):
        vh = VirtualMachineHandler(token)
        if vh.conn is None:
            return {"message": vh.STATUS}, 403
        try:
            if type == "ssh":
                new_rule = vh.conn.network.create_security_group_rule(
                            direction="ingress",
                            protocol="tcp",
                            port_range_max=22,
                            port_range_min=22,
                            security_group_id=security_group_id,
                            ether_type="IPv4",

                        )
            if type == "all_icmp":
                new_rule = vh.conn.network.create_security_group_rule(
                    direction="ingress",
                    protocol="ICMP",
                    security_group_id=security_group_id,
                    ether_type="IPv4",
                    remote_ip_prefix="0.0.0.0/0")

            return new_rule.to_dict(), 201
        except Exception as e:
            return {"message": str(e)}, 409

    def get(self, token, security_group_id, security_group_rule_id):
        return {}, 501

    def list(self, token, security_group_id):
        return {}, 501

    def update(self, token, security_group_id):
        return {}, 501

    def delete(self, token, security_group_id):
        return {}, 501