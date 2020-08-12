from pprint import pprint
#todo remove this file
from Token import token
from requests import get

pprint(get("http://127.0.0.1:5000/instances/", json={"token": token}).json())
