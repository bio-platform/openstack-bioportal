from marshmallow import Schema, fields, validate
from openstack_resources import connection_types


class SecurityGroupSchema(Schema):
    name = fields.String(required=False, default="default_security_group")


class SecurityGroupRuleSchema(Schema):
    type = fields.String(required=True, validate=validate.OneOf(connection_types))
    security_group_id = fields.String(required=True)

