from keystoneauth1 import session
from keystoneauth1.identity.v3 import ApplicationCredential
from keystoneauth1.identity.v3.oidc import OidcAccessToken
from keystoneauth1.identity.v3 import Token
# https://docs.openstack.org/keystoneauth/latest/api/keystoneauth1.identity.v3.html#module-keystoneauth1.identity.v3
"""
#auth = ApplicationCredential(application_credential_id='9b7f229b8c654aeea8c522548f02bc17', application_credential_secret='Vp5Et0eCKlfeiwFhyeSK5VdMbmt3wl5hJNClqBgLy_vID209bcmx8xMCWjaEwQfCl7UDQ-HgDd2RkXeCQMwJrg', auth_url ="https://identity.cloud.muni.cz/v3/")
admin = ApplicationCredential(application_credential_id='e2fdf90a78cd4275a9bf16abc9e14556',
                              application_credential_secret="uQfwUhxMAi0Y2meY3oUyfS8RYcJJLkZwc7sCzSq6L3w-JBefAt6OD6J1RW7ro-eubNzIONaULXUY21bd4VXJpg",
                              auth_url ="https://identity.cloud.muni.cz/v3")
sess = session.Session(auth=admin)
print(admin.get_token(session=sess))
"""
admin = OidcAccessToken(auth_url="https://identity.cloud.muni.cz/v3",
                       identity_provider="login.cesnet.cz",
                       protocol="openid",
                       access_token="eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY0OTk0MDA2LCJpYXQiOjE1NjQ5OTA0MDYsImp0aSI6ImM1OTgwM2NjLWIzNDgtNDRiMy1iYjk3LTMzMTI1NjI2NWM2MiJ9.VSrCWGSy5fCqZwaF_4_6E0Vqa4eH_kzyP8EX-fMcybaEeeY8lQ001r3CHyj47rzujhEvYC0LtMyWHSsaIOzMBKg0j2snIV6qSqyicvoqPOSlmrHN90f35DGxQzCcqdVw66QfgPR4MVFSM65xQf6Yg26Dt39S6N-jBy3CRMz3K93HYWVCPZh94qRqVim3XJpGbVkyeBRgmFXCU4_GPOW7iHFu7i24gLuU1sS1EVsr1v_4SVT41v4Z5bxllnkYUaNgo2eAmo4LaoqjV9HH_PrVKQno5DXldeg-3SnH9FcLz6sNZtUmhpVeKvcB_JcuyMeV6L_Jq2Zy_v9HDcr9DLioEw")
sess = session.Session(auth=admin)
token = admin.get_token(sess)
print(token)

t = Token(auth_url="https://identity.cloud.muni.cz/v3",
          token=token,
          project_domain_name="einfra_cz",
          project_name="dbc23d6dbd554be659114117efd4faf0f57466f4@einfra.cesnet.cz")
from openstack import connection
sesss = session.Session(auth=t)
conn = connection.Connection(session=sesss)
conn.authorize()
print(t.get_token(sesss))
print(conn.compute.servers())
for f in conn.compute.servers():
    print(f)