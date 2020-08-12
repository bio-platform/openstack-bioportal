from requests import get, post, put
from pprint import pprint
from Token import token

# print(put("http://localhost:5000/security_group/", json={"name": "new1"}).json())
pprint(post("http://localhost:5000/security_groups/cecb51c0-adc4-42b7-ba65-de374d813d7a/security_group_rules/",
            json={"type": "ssh",
                  "token": token}).json())
pprint(get("http://localhost:5000/security_groups/cecb51c0-adc4-42b7-ba65-de374d813d7a",
           json={"token": token}).json())
