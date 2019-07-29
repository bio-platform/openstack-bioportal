from requests import get, post
from pprint import pprint
pprint(get("http://localhost:5000/security_group/cecb51c0-adc4-42b7-ba65-de374d813d7a/").json())
