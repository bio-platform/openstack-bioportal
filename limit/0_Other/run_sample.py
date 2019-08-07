from requests import get
from Token import token
print(get("http://127.0.0.1:5000/limits/", json={"token": token}).json())