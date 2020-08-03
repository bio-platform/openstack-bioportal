from keystoneauth1 import session
from keystoneauth1.identity.v3 import OidcAccessToken, Token
from openstack import connection
from oslo_utils import encodeutils
from requests import get


class VirtualMachineHandler:

    def create_connection(self):
        try:
            admin = OidcAccessToken(auth_url=self.AUTH_URL,
                                    identity_provider=self.IDENTITY_PROVIDER,
                                    protocol=self.PROTOCOL,
                                    access_token=self.ACCESS_TOKEN)

            sess = session.Session(auth=admin)
            conn = connection.Connection(session=sess)

            unscoped_token = conn.authorize()
            user_id = admin.get_user_id(sess)

            projects = get("https://identity.cloud.muni.cz/v3/users/%s/projects" % user_id,
                           headers={"Accept": "application/json",
                                    "User-Agent": "Mozilla/5.0 (X11;",
                                    "X-Auth-Token": unscoped_token}).json()['projects']
            if projects:
                self.PROJECT_ID = projects[0]["id"]
                self.PROJECT_DOMAIN_ID = projects[0]["domain_id"]

            t = Token(auth_url=self.AUTH_URL,
                      token=unscoped_token,
                      project_domain_id=self.PROJECT_DOMAIN_ID,
                      project_id=self.PROJECT_ID)

            sess = session.Session(auth=t)
            conn = connection.Connection(session=sess)

        except Exception as e:
            # raise Exception('Client failed authentication at Openstack Reason: {}'.format(e))
            self.STATUS = 'Client failed authentication at Openstack Reason: {}'.format(e)
            return None
        self.SESSION = sess
        return conn

    def __init__(self, access_token):
        self.AUTH_URL = "https://identity.cloud.muni.cz/v3"
        self.ACCESS_TOKEN = access_token
        self.IDENTITY_PROVIDER = "login.cesnet.cz"
        self.PROTOCOL = "openid"
        self.NETWORK = None
        self.SESSION = None
        self.PROJECT_DOMAIN_ID = None
        self.PROJECT_ID = None
        self.STATUS = None
        self.conn = self.create_connection()
