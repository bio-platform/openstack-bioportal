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
                       access_token="eyJqa3UiOiJodHRwczpcL1wvbG9naW4uY2VzbmV0LmN6XC9vaWRjXC9qd2siLCJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkYmMyM2Q2ZGJkNTU0YmU2NTkxMTQxMTdlZmQ0ZmFmMGY1NzQ2NmY0QGVpbmZyYS5jZXNuZXQuY3oiLCJhenAiOiJmYTA0MGY5ZS1hZTViLTRmYzItOWNlYS03ZmFiNjcxMmM3NzMiLCJzY29wZSI6ImVkdVBlcnNvbkVudGl0bGVtZW50IGZvcndhcmRlZEVudGl0bGVtZW50IG9wZW5pZCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIiwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLmNlc25ldC5jelwvb2lkY1wvIiwiZXhwIjoxNTY0MDUyODA0LCJpYXQiOjE1NjQwNDkyMDQsImp0aSI6ImE3M2JjN2UwLTk3ZDgtNDQ4My04ZDI1LWI1YzRjNDU1ZjZlNiJ9.Dm7gRNIMcrHTwbIrD2wMgc_9R0zN-JWF0xuES9RpgDMqMMENxDe3HzNNQTckZGw6EgqCR-llf3SmRKHVh1nq9F_tPHZQW9o1Xi7vOZrzHtaPbtmDoR8QET-2yhHr5_inLsGIViV5rO6HGXDsS9D7DJPBoFDGpTvxsdc_RKDLuI-ewXU7wuVNW8G0_a2gS-5Ji3thI8U3UphmIMKcajXdsyiLhPcJH-WYoCGElQ5UtbJwx6FTEovDqFHEzBAs_awIguJrsq07dDEhiOBX2FYWlPdpJyp6Zopi4CAERphko66UUM1jMovewXvJl53MaPrOx_I1UTiE6pgBHgY6DxVK4g")
sess = session.Session(auth=admin)
token = admin.get_token(sess)
print(admin.get_headers(sess))
t = Token(auth_url="https://identity.cloud.muni.cz/v3",
          token=token,
          project_domain_id="5c50ee4cfcae43d289aa832475556f8e",
          project_name="dbc23d6dbd554be659114117efd4faf0f57466f4@einfra.cesnet.cz")
print(token)
from openstack import connection
sesss = session.Session(auth=t)
conn = connection.Connection(session=sesss)
conn.authorize()
print(conn.compute.flavors())
