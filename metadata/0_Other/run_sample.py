from Token import token
from requests import put, delete

print(put("http://127.0.0.1:5000/metadata/71c053da-e598-4fa8-8577-55b863f888b5/",
          json={"metadata": {"metadata_1": "abc"},
                "token": token}).json())

print(delete("http://127.0.0.1:5000/metadata/71c053da-e598-4fa8-8577-55b863f888b5/",
             json={"keys": ["metadata_1"],
                   "token": token}))
# print(get("http://127.0.0.1:5000/metadata/71c053da-e598-4fa8-8577-55b863f888b5/", json={"token": token}).json())
# "kys": ["sw_database_cassandra_version"]metadata/
