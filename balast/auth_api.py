from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from keystoneauth1.identity.v3 import Token
from openstack import connection
from requests import get

admin = OidcAccessToken(auth_url="https://identity.cloud.muni.cz/v3",
                       identity_provider="login.cesnet.cz",
                       protocol="openid",
                       access_token="eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY1MTc0ODQzLCJpYXQiOjE1NjUxNzEyNDMsImp0aSI6Ijc4MjUzMTY2LTRmZTktNDkxYS1hN2ZmLTZhMzM2Mjk4MDVlMyJ9.OEuBhi3Dl5SiSjq37PRzO7L3Dkf9ITiJVW_puslNAcjP7-siQQskX3nS2Ds4SQbUTCHFzMIEcy057B4IeO2uHi9HjQeoljQSkEvO9Vh_rvBaYXDPP3DqHpfzp4mAaIEbcVYr6jP1XRVRQjQ7kdyc-xgMDVKet78ApMOFmU7-e5EuY09TKRGtygDdpXhgv4fV0Yzw7S_MMvZg2jPfYLN0casZAiTbrrCOlQStK_UJbohlumk9JiA-iCwwcRGtn0T-DBwQ-5Bt088v5jMWxOk1i6G_GuEfokN06EPzjHDYhluRwYYQQpeEb1t6vd_DAkpNRXkJ2xx3Pg9k8fDfZtfqJQ")

sess = session.Session(auth=admin)
conn = connection.Connection(session=sess)
unscoped_token = conn.authorize()

print(unscoped_token)
t = Token(auth_url="https://identity.cloud.muni.cz/v3",
          token=unscoped_token,
          project_domain_id="f9ec246d5e81496b921be023ee9ac672")
# ,,
#
#           project_id="5c50ee4cfcae43d289aa832475556f8e"
# print(t.get_auth_ref(sess1).system_scoped)
sess1 = session.Session(auth=t)

user_id = t.get_user_id(sess)

print("4a8f9a18d56d4d9e84c42d20c8b0aad6" == user_id)
projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % user_id, headers={"Accept": "application/json",
                                                                                 "User-Agent": "Mozilla/5.0 (X11;\
                                                                                  Ubuntu; Linux x86_64; rv:68.0)\
                                                                                   Gecko/20100101 Firefox/68.0",
                                                                                 "X-Auth-Token": unscoped_token}).json()
#print(projects["id"], projects["domain_id"], projects["name"])
print(projects["projects"])
# user = conn.identity.get_u.json()ser(user=user_id)

conn = connection.Connection(session=sess1, interface='public')
projects = conn.identity.user_projects(user=user_id)
for p in projects:
    print(p.id)
"""openstack token issue --os-project-name=dbc23d6dbd554be659114117efd4faf0f57466f4@einfra.cesnet.cz --os-project-domain-name=einfra_cz
"""