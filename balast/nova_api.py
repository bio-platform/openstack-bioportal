import inspect
from pprint import pprint

from datetime import datetime, timedelta
from novaclient import client
from auth_api import sess
import os
import time
from requests import get
from glance_api import glance_client
#https://docs.openstack.org/python-novaclient/latest/reference/api/index.html
from auth_api import admin
from novaclient.v2 import flavors

nova = client.Client(2, session=sess)
token = admin.get_token(session=sess)
def start_new_instance(key,instance_name, image_name, flavor_name, glance_client, nova_client):

    if not nova_client.keypairs.findall(name=key):
        with open(os.path.expanduser('~/home/id_rsa.pub')) as fpubkey:
            nova_client.keypairs.create(name=key, public_key=fpubkey.read())

    image = glance_client.images.list()
    image_list = [i for i in image]
    image = list(filter(lambda x: x.name.find(image_name) != -1, image_list))
    if not image:
        return None

    flavor = nova_client.flavors.find(name=flavor_name)
    instance = nova_client.servers.create(name="instance_name", image=image[0], flavor=flavor, key_name=key)

    # Poll at 5 second intervals, until the status is no longer 'BUILD'
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
    print("status: %s" % status)

def shut_down_instance(nova):
    server = nova.servers.list()[0]
    server.delete()
"""
# start_new_instance("myKey1", "instance1", "cirros-0.4.0-x86_64", "standard.medium", glance_client, nova)
subnet = get("https://network.cloud.muni.cz/v2.0/subnets",
                headers={"X-Auth-Token": token}).json()['subnets']

usage = nova.usage.get(subnet[0]["tenant_id"], datetime.now()-timedelta(200), datetime.now())
limits = nova.limits.get(tenant_id = subnet[0]["tenant_id"])
pprint(usage.to_dict())
pprint(limits.to_dict())
"""
#server = nova.servers.list()
#pprint([s.to_dict() for s in server])

#volume = nova.volumes.get_server_volumes(server_id=server.to_dict()['id'])
#pprint(dir(volume))
# print(nova.usage.list(datetime.now()-timedelta(200), datetime.now())) #not allowed
# print(nova.availability_zones.list()) #not allowed
# print(nova.migrations.list()) #not allowed
# wtf print(nova.shell.do_agent_list())
# print(nova.cells.capacities()) # not implemented

#print(nova.server_groups.list())
#print(nova.versions.get_current())
#print(nova.flavors.list())




# pairs

#keypairs = nova.keypairs.list()
#print(keypairs[1].name, keypairs[1].public_key, keypairs[1].id)

# nova.keypairs.create("new_keypair")
# nova.keypairs.delete("new_keypair")
# print(nova.keypairs.list())

#nedela - 3h
#utorok - 9h