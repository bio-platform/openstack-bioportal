from requests import put,delete

#print(put("http://127.0.0.1:5000/71c053da-e598-4fa8-8577-55b863f888b5/", json={"metadata_1": "abc"}).json())
print(delete("http://127.0.0.1:5000/71c053da-e598-4fa8-8577-55b863f888b5/", json={}).json())
#"kys": ["sw_database_cassandra_version"]