from pprint import pprint

from requests import get

# print(post("http://127.0.0.1:5000/floating_ip/", json={"network_id": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe",
#                                                       "instance_id": "71c053da-e598-4fa8-8577-55b863f888b5"}))

pprint(get("http://127.0.0.1:5000/limits/", headers={
    "Cookie": "session=.eJwVys1ugjAAAOB36dklBCgUbzBHIpV_CcKlKbQgQwtiVcDs3bd95-8NyMinKxVcSLCV04NvwDgN37yWpGNgC2ANFc71uqkp1zWmIotSpKm6CSE0GsTBBsih5-KvtvY_hxUflb2_9WuVv3y3GEhzrBInna0FMzs5YCyUdu0CUZ6cu5p66KA_77Qy50uZO3HOHPnIJuNWPg1EEA7FqaA-888aPnoR7JYkpp4ZhIIHOVELZX-WoXAnN3rFmbVcBzH2O4NkwTrvhOXBFAVfEaYtutDqU9rg5xf7rk8r.EEV4QA.GdxO232fw-8M7HNgFc2sp-8UFz0; Expires=Mon, 26-Aug-2019 16:50:24 GMT; HttpOnly; Path=/"}).json())

# print(put("http://127.0.0.1:5000/gateways/8594d608-dd3f-4567-b0e0-d6dd44468801/",
#    json={"external_network": "d896044f-90eb-45ee-8cb1-86bf8cb3f9fe", "token": token}).json())
