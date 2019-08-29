from keystoneauth1 import session
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from keystoneauth1.identity.v3 import Token
from openstack import connection
from requests import get
"""
oidc_token = "eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGVkdV9wZXJzb25fZW50aXRsZW1lbnRzIGVtYWlsIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY1ODU5Mjk2LCJpYXQiOjE1NjU4NTU2OTYsImp0aSI6IjRhNjA4MWU2LWZlZDQtNDhhNi05MjU5LTg0MTQ0MjVhODczOCJ9.TUiw-GnktBONynUareAvxM4j9Aq7AZGI9ODnBlzM_StoZ9v1A_ZyHEgpZU7ieVROYlL26Yx-1K2LE0mOtR60a1eJMHj8-6M4y1Au4YR4uyqy3OJDNPiGrA617oOR08_5g1xy-Kagsn2WY7LeICLUctrr2XW2gB_hsKZR2lrHdPWZf2nJBNb2Pne9TNOGnGe0NgVA41xO7wSoalNLunPuyjf6sH4fHVj87NzlFxvT13CvxHuNQOqdiLmwf3jFzE3Pc3rQ-KCdurzUyD4m_27RYzvLyIWDjjncvrwgdcUwC5hkgNNStYMGqEDJCJlWjhzDAU_q8n-agkVudDGTRo10Vw"
admin = OidcAccessToken(auth_url="https://identity.cloud.muni.cz/v3",
                       identity_provider="login.cesnet.cz",
                       protocol="openid",
                       access_token=oidc_token)

sess = session.Session(auth=admin)
conn = connection.Connection(session=sess)
unscoped_token = conn.authorize()

user_id = admin.get_user_id(sess)


projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % user_id, headers={"Accept": "application/json",
                                                                                 "User-Agent": "Mozilla/5.0 (X11;\
                                                                                  Ubuntu; Linux x86_64; rv:68.0)\
                                                                                   Gecko/20100101 Firefox/68.0",
                                                                                 "X-Auth-Token": unscoped_token}).json()
print(projects["projects"])

print(unscoped_token)
t = Token(auth_url="https://identity.cloud.muni.cz/v3",
          token=unscoped_token,
          project_domain_id="f9ec246d5e81496b921be023ee9ac672",
          project_id=projects['projects'][0]['id'])

sess1 = session.Session(auth=t)
scoped = t.get_token(sess1)

conn = connection.Connection(session=sess1)
print(conn.compute.get_limits())

print(scoped)

"""
from datetime import datetime
t = datetime.now()

print(datetime.now() - t)
print(conn.compute.get_limits())
"""openstack token issue --os-project-name=dbc23d6dbd554be659114117efd4faf0f57466f4@einfra.cesnet.cz --os-project-domain-name=einfra_cz

"""