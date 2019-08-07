from marshmallow import Schema, fields, validate
from openstack_resources import connection_types
from DefaultSchema import DefaultSchema


class SecurityGroupSchema(DefaultSchema):
    name = fields.String(required=False, default="default_security_group")


class SecurityGroupRuleSchema(DefaultSchema):
    type = fields.String(required=True, validate=validate.OneOf(connection_types))

