from requests import get, put, post
"""
res = post("http://localhost:5050/keypairs/",
           json={"public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ andrej",
                 "keyname": "key1"})
print(res.status_code, res.json())
assert res.status_code//100 == 2

sec_group = get("http://localhost:5050/security_groups/").json()[1]

print((sec_group["id"]))
res = post("http://localhost:5050/security_groups/%s/security_group_rules/" %sec_group["id"], json={"type": "ssh"})

print(res.status_code, res.json())
assert res.status_code//100 == 2

res = post("http://localhost:5050/security_groups/%s/security_group_rules/" %sec_group["id"], json={"type": "all_icmp"})

print(res.status_code, res.json())
assert res.status_code//100 == 2
"""
create_request = {
    "image": "cirros-0.4.0-x86_64",
    "flavor": "standard.small",
    "key_name": "key1",
    "servername": "new_instance_via_api",
    "network_id": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe",
    "token": "token",
}

instance = post("http://localhost:5050/instances/", json=create_request)
print(instance.status_code)
assert instance.status_code == 201

res = put("http://localhost:5050/gateways/8594d608-dd3f-4567-b0e0-d6dd44468801/",
          json={"external_network": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe"})

assert res.status_code/100 == 2

res = post("http://localhost:5050/floating_ips/", json= {"network_id": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe",
                                                  "instance_id": instance.json()["id"]})

assert res.status_code/100 == 2

print("DONE!!!")
