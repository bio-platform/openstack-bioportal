from pprint import pprint

from Token import token
from requests import get

pprint(get("http://127.0.0.1:5000/instances/", json={"token": token}).json())
