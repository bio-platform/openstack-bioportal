from flask import Flask
from flask_restful import Api
from security_group.APISecurityGroup.SecurityGroupManager import SecurityGroupManager
from security_group.APISecurityGroup.SecurityGroupRuleManager import SecurityGroupRuleManager

app = Flask(__name__)
api = Api(app)

api.add_resource(SecurityGroupManager, '/security_group/', '/security_group/<string:security_group_id>/')
api.add_resource(SecurityGroupRuleManager,
                 '/security_group/<string:security_group_id>/security_group_rule/',
                 '/security_group/<string:security_group_id>/security_group_rule/<string:security_group_rule_id>/')

if __name__ == '__main__':  
    app.run(debug=True)