from balast.ssh import pubkey
from VirtualMachineHandler import VirtualMachineHandler
from pprint import pprint
from requests import get
# access_token = "eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY0MDUwMDkyLCJpYXQiOjE1NjQwNDY0OTIsImp0aSI6ImQ0MjNlNTBkLTExYTctNDk0Yi1iY2NmLTY0MmM2YmJlNTNmNiJ9.LGg711xDVAPy5Wk4sLj8IbQRgn55koGrMzot4CQfzxx1D5OsbUwDbV8GLEGHkEyrrCq5t84INIJ2buwEWO918byFHGJhsH0i-LGCMjQ7KYhY6fsSPhkF2ZGKwDOtpiN_-2i2kM7zjgSsGLB12xV7fW8v1Agv99t24u4WaKEPxSTtpxHufKYyU5NrNXlY8JaVNtA81J0RGFUg-ZKOqsa_EFDRmPg9CkIW3AyTgHgQ4kPddVD4lCN-GPHWSHqP3N84ylzRnK0Yg_aJ5CxSVP8AMR-D3rt4aG9qaEO-mxPjFzLcGydrFY-GnraMoc75hjUV1vQkiv8YC2cq7UFPATErww"
# vm_handler = VirtualMachineHandler(access_token=access_token, config="clouds.yaml")
vm_handler = VirtualMachineHandler("aa", "clouds.yaml")
#pprint(vm_handler.conn.compute.get_server_metadata("71c053da-e598-4fa8-8577-55b863f888b5"))
#pprint(vm_handler.conn.get_server("71c053da-e598-4fa8-8577-55b863f888b5"))
token = vm_handler.conn.authorize()
pprint(vm_handler.conn.compute.get_limits())
quotas = get("https://network.cloud.muni.cz/v2.0/quotas/%s/details.json" % "5c50ee4cfcae43d289aa832475556f8e",
                headers={"X-Auth-Token": token}).json()
pprint(quotas)

"""
vm_handler = VirtualMachineHandler("clouds.yaml")
vm_handler.import_keypair("new_keypair", pubkey)

sec_group_id = vm_handler.get_security_group("default").id
vm_handler.add_security_group_rule("ssh", sec_group_id)
vm_handler.add_security_group_rule("all_icmp", sec_group_id)

new_instance = vm_handler.start_server("standard.small",
                        "cirros-0.4.0-x86_64",
                        "new_keypair",
                        pubkey,
                        "new_server",
                        "0",
                        "new_vol")

vm_handler.add_gateway_to_router('8594d608-dd3f-4567-b0e0-d6dd44468801',
                              "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe")
vm_handler.add_floating_ip_to_server(new_instance["openstackid"]["id"],
                                     "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe")

"""

"""
nova = client.Client(2, session=sess)
token = admin.get_token(session=sess)

project_id = "5c50ee4cfcae43d289aa832475556f8e"

quotas = get("https://network.cloud.muni.cz/v2.0/quotas/%s/details.json" % project_id,
                headers={"X-Auth-Token": token}).json()
pprint(quotas)



networks_response = get("https://network.cloud.muni.cz/v2.0/networks",
                headers={"X-Auth-Token": token})
if networks_response.status_code == 200:
    networks = networks_response.json()["networks"]
else:
    raise Exception('Error when retrieving networks \n Reason: {}'.format(networks_response.reason))

networks = list(filter(lambda x: x["project_id"] == project_id, networks))

if not networks:
    # no need to create new
    raise Exception('Error, no network found')


pprint(networks)
"""