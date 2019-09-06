from flask import Flask
from flask_restful import Api
from limit.APILimit.LimitManager import LimitManager
from security_group.APISecurityGroup.SecurityGroupManager import SecurityGroupManager
from security_group.APISecurityGroup.SecurityGroupRuleManager import SecurityGroupRuleManager
from network.APINetwork.GatewayManager import GatewayManager
from network.APINetwork.FloatingIpManager import FloatingIpManager
from network.APINetwork.NetworkManager import NetworkManager
from metadata.APIMetadata.MetadataManager import MetadataManager
from keypair.APIKeypair.KeypairManager import KeypairManager
from instance.APIInstance.InstanceManager import InstanceManager
from network.APINetwork.RouterManager import RouterManager
from project.APIProject.ProjectManager import ProjectManager
from login.APILogin.LoginManager import LoginManager
import os

app = Flask(__name__)

app.secret_key = os.urandom(12).hex()
api = Api(app)
app.permanent_session_lifetime = 10000

api.add_resource(LimitManager, '/limits/')

api.add_resource(SecurityGroupManager, '/security_groups/', '/security_groups/<string:security_group_id>/')
api.add_resource(SecurityGroupRuleManager,
                 '/security_groups/<string:security_group_id>/security_group_rules/',
                 '/security_groups/<string:security_group_id>/security_group_rules/<string:security_group_rule_id>/')

api.add_resource(GatewayManager, '/gateways/', '/gateways/<string:router_id>/')
api.add_resource(FloatingIpManager, '/floating_ips/', '/floating_ips/<string:floating_ip_id>/')
api.add_resource(NetworkManager, '/networks/', '/networks/<string:network_id>/')

api.add_resource(MetadataManager, '/metadata/<string:instance_id>/')

api.add_resource(KeypairManager, '/keypairs/', '/keypairs/<string:keypair_id>/')

api.add_resource(InstanceManager, '/instances/', '/instances/<string:instance_id>/')

api.add_resource(RouterManager, '/routers/', '/routers/<string:router_id>/')

api.add_resource(ProjectManager, '/projects/')

api.add_resource(LoginManager, '/')

if __name__ == '__main__':
    app.run()
