from auth_api import sess, admin
from nova_api import start_new_instance, nova, glance_client
from novaclient import client
from requests import get, post, put
from pprint import pprint
from time import sleep
from ssh import pubkey as local_public_key
token = admin.get_token(session=sess)

new_keypair = "new_keypair"


nova_client = client.Client(2, session=sess)
networks = get("https://network.cloud.muni.cz/v2.0/networks",
                headers={"X-Auth-Token": token}).json()['networks']
private_muni = list(filter(lambda x: x["name"].find("private-muni") != -1, networks))


subnet = get("https://network.cloud.muni.cz/v2.0/subnets",
                headers={"X-Auth-Token": token}).json()['subnets']


router_gateway_request = {"router": {
                    "external_gateway_info":{
                        "network_id": private_muni[0]["id"]
                    }
                }
}
print(private_muni[0]["id"])
router_id = get("https://network.cloud.muni.cz/v2.0/routers",
                headers={"X-Auth-Token": token}).json()['routers'][0]['id']
#put("https://.cloud.muni.cz/v2.0/routers/%s" % router_id,
#                headers={"X-Auth-Token": token}, json = router_gateway_request).json()



"""
# Create Key Pair using local public key
print("CREATING Key Pair")
nova_client.keypairs.create(new_keypair, public_key=local_public_key)
keypairs = nova_client.keypairs.list()


# Update Security Group
print("UPDATING Security Group")
sec_group = get("https://network.cloud.muni.cz/v2.0/security-groups",
                headers={"X-Auth-Token": token}).json()['security_groups']

print("ADDING SSH RULE")
request_data = {
    "security_group_rule": {
        "direction": "ingress",
        "port_range_min": "22",
        "ethertype": "IPv4",
        "port_range_max": "22",
        "protocol": "tcp",
        "security_group_id": sec_group[0]["id"]
    }
}

post("https://network.cloud.muni.cz/v2.0/security-group-rules",
           headers={"X-Auth-Token": token}, json=request_data).json()

print("ADDING ALL ICMP RULE")
request_data = {
    "security_group_rule": {
        "direction": "ingress",
        "ethertype": "IPv4",
        "protocol": "ICMP",
        "security_group_id": sec_group[0]["id"],
        "remote_ip_prefix": "0.0.0.0/0"
    }
}
post("https://network.cloud.muni.cz/v2.0/security-group-rules",
           headers={"X-Auth-Token": token}, json=request_data).json()



print("CREATING Virtual Machine Instance")
start_new_instance(new_keypair, "new_instance", "cirros", "standard.small", glance_client, nova)

# Setup Router gateway
print("SETTING UP Router Gateway")
router_gateway_request = {"router": {
                    "external_gateway_info":{
                        "network_id": private_muni[0]["id"]
                    }
                }
}

router_id = get("https://network.cloud.muni.cz/v2.0/routers",
                headers={"X-Auth-Token": token}).json()['routers'][0]['id']
put("https://network.cloud.muni.cz/v2.0/routers/%s" % router_id,
                headers={"X-Auth-Token": token}, json = router_gateway_request).json()

print("ALLOCATING Floating IP")

subnet = get("https://network.cloud.muni.cz/v2.0/subnets",
                headers={"X-Auth-Token": token}).json()['subnets']

servers = nova_client.servers.list()[0]
port = get("https://network.cloud.muni.cz/v2.0/ports/",
                headers={"X-Auth-Token": token}).json()['ports'][1]

req = {
    "floatingip": {
        "floating_network_id": private_muni[0]["id"],
        "project_id": subnet[0]["project_id"], # treba zistit ako rozumne ziskat tieto IDS, takto jeto zle
        "tenant_id": subnet[0]["tenant_id"]
    }
}
floatingip_data = post("https://network.cloud.muni.cz/v2.0/floatingips",
                       headers={"X-Auth-Token": token}, json=req).json()['floatingip']

print("ASSOCIATING Floating IP with INSTANCE")
update_request = {
    "floatingip": {
        "port_id": port["id"],
    }
}
put("https://network.cloud.muni.cz/v2.0/floatingips/%s" % floatingip_data["id"],
                headers={"X-Auth-Token": token}, json=update_request).json()


print("CREATING volume")

create_volume_request = {"volume":
    {
        "size": 10,
        "description": "new_vol1",
        "name": "new_volume1"
    }
}
volume = post("https://volume.cloud.muni.cz/v3/5c50ee4cfcae43d289aa832475556f8e/volumes",
            headers={"X-Auth-Token": token}, json=create_volume_request).json()['volume']

status = get("https://volume.cloud.muni.cz/v3/5c50ee4cfcae43d289aa832475556f8e/volumes/%s" % volume['id'],
            headers={"X-Auth-Token": token}).json()['volume']["status"]

while status == 'creating':
    sleep(5)
    # Retrieve the instance again so the status field updates
    status = get("https://volume.cloud.muni.cz/v3/5c50ee4cfcae43d289aa832475556f8e/volumes/%s" % volume['id'],
                 headers={"X-Auth-Token": token}).json()['volume']["status"]

print("status: %s" % status)
"""
# Attach volume to instance
"""
servers = nova.servers.list()
servers = [server.to_dict() for server in servers]
volume = get("https://volume.cloud.muni.cz/v3/5c50ee4cfcae43d289aa832475556f8e/volumes",
            headers={"X-Auth-Token": token}).json()['volumes'][0]
# pprint(servers)
pprint(volume)
attach_volume_request = {
    "os-detach": {
        "mountpoint": "/dev/sdb",
        "instance_uuid": servers[0]["id"],

    }
}#5c50ee4cfcae43d289aa832475556f8e
pprint(post("https://volume.cloud.muni.cz/v3/5c50ee4cfcae43d289aa832475556f8e/volumes/%s/action" % volume["id"],
            headers={"X-Auth-Token": token}, json=attach_volume_request).reason)

"""