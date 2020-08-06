from flask import Flask
from flask_restful import Api
from resources.limit import Limit
from resources.security_group import SecurityGroup
from resources.security_group_rule import SecurityGroupRule
from resources.gateway import Gateway
from resources.floating_ip import FloatingIp
from resources.network import Network
from resources.metadata import Metadata
from resources.keypair import Keypair
from resources.instance import Instance
from resources.router import Router
from resources.project import Project
from resources.login import Login
import os
import logging

from openstack.exceptions import HttpException
#from werkzeug.exceptions import HTTPException
app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('Gunicorn logging start')
app.secret_key = os.urandom(12).hex()

api = Api(app)
app.permanent_session_lifetime = 10000


@app.errorhandler(HttpException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error

    app.logger.info("Exception handled")
    #response.content_type = "application/json"
    return {}, 400

api.add_resource(Limit, '/limits/')

api.add_resource(SecurityGroup, '/security_groups/', '/security_groups/<string:security_group_id>/')
api.add_resource(SecurityGroupRule,
                 '/security_groups/<string:security_group_id>/security_group_rules/',
                 '/security_groups/<string:security_group_id>/security_group_rules/<string:security_group_rule_id>/')

api.add_resource(Gateway, '/gateways/', '/gateways/<string:router_id>/')
api.add_resource(FloatingIp, '/floating_ips/', '/floating_ips/<string:floating_ip_id>/')
api.add_resource(Network, '/networks/', '/networks/<string:network_id>/')

api.add_resource(Metadata, '/metadata/<string:instance_id>/')

api.add_resource(Keypair, '/keypairs/', '/keypairs/<string:keypair_id>/')

api.add_resource(Instance, '/instances/', '/instances/<string:instance_id>/')

api.add_resource(Router, '/routers/', '/routers/<string:router_id>/')

api.add_resource(Project, '/projects/')

api.add_resource(Login, '/')

if __name__ == '__main__':
    app.run()
