from keystoneclient.v3 import client
from auth_api import sess

print(dir(sess))
print(sess.app_name)
# needs to by UNRESTRICTED
keystone_client = client.Client(session=sess, endpoint_override="https://identity.cloud.muni.cz/v3/")
# user_role = keystone_client.roles.create("user")
#print(keystone_client.roles.list())
#print(keystone_client.projects.list())
try:
    print(keystone_client.credentials.list())
except Exception as e:
    print(e)
    print(e.url)