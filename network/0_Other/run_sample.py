from requests import put, get, post

#print(post("http://127.0.0.1:5000/floating_ip/", json={"network_id": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe",
#                                                       "instance_id": "71c053da-e598-4fa8-8577-55b863f888b5"}))

print(get("http://127.0.0.1:5050/network/1fd8ee12-75fa-40d1-b218-8278e22fd3b6/"))

print(get("http://127.0.0.1:5000/network/gateway/8594d608-dd3f-4567-b0e0-d6dd44468801/",
    json={"external_network": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe"}))