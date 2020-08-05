from keystoneauth1.identity.v3 import Token
from keystoneauth1 import session
from openstack import connection
from openstack_resources import AUTH_URL, PROJECT_DOMAIN_ID


def connect(token, project_id):
    user = Token(auth_url=AUTH_URL,
                 token=token,
                 project_domain_id=PROJECT_DOMAIN_ID,
                 project_id=project_id)

    sess = session.Session(auth=user)
    conn = connection.Connection(session=sess)
    conn.authorize()

    return conn
