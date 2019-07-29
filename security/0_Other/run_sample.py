from requests import get, post, put
from pprint import pprint
pprint(put("http://localhost:5000/security_group/", json={"name": "new1"}).json())
pprint(post("http://localhost:5000/security_group_rule/", json={"type": "ssh",
                                                                "security_group_id": "381ffa85-4169-47ac-9092-21bf18120a22"}).json())
