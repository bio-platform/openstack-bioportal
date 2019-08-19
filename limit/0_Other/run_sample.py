from requests import get, put
from Token import token
print(put("http://127.0.0.1:5000/limits/", json={"token": token}).json())
print(put("http://127.0.0.1:5000/limits/", json={"token": token}).request)
