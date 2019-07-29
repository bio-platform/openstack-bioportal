from requests import get
from pprint import pprint

pprint(get("http://127.0.0.1:5000/").json())
