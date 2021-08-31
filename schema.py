from marshmallow import Schema, fields, validate
from openstack_resources import connection_types

"""Set of all marshmallow schemes used in this project"""
class StartTerraformSchema(Schema):
    name = fields.String(required=True)
    input_variables = fields.Dict(required=True)

class DeleteTerraformSchema(Schema):
    name = fields.String(required=True)
    workspace_id = fields.String(required=True)

class StartServerSchema(Schema):
    flavor = fields.String(required=True)
    image = fields.String(required=True)
    key_name = fields.String(required=True)
    # public_key = fields.String(required=True)
    servername = fields.String(required=True)
    network_id = fields.String(required=True)
    diskspace = fields.Int(required=False, default=0)
    volume_name = fields.String(required=False, default="new_volume")
    metadata = fields.Dict(required=True)


class CreateMetadataSchema(Schema):
    metadata = fields.Dict(required=True)


class DeleteMetadataSchema(Schema):
    keys = fields.List(fields.String(), required=True)


class CreateKeypairSchema(Schema):
    public_key = fields.String(required=False)
    name = fields.String(missing="default_key")


class NetworkSchema(Schema):
    external_network = fields.String(required=True)


class TerraformAttachIP(Schema):
    user_email = fields.String(required=True)
    floating_ip = fields.String(required=True)
    instance_id = fields.String(required=True)

class FloatingIpSchema(Schema):
    network_id = fields.String(required=True)
    instance_id = fields.String(required=True)


class ProjectSchema(Schema):
    unscoped_token = fields.String(required=True)
    user_id = fields.String(required=True)


class SecurityGroupSchema(Schema):
    name = fields.String(required=False, default="default_security_group")


class SecurityGroupRuleSchema(Schema):
    type = fields.String(required=True, validate=validate.OneOf(connection_types))


class LoginSchema(Schema):
    token = fields.String(required=True)


class ScopeSchema(Schema):
    project_id = fields.String(required=True)
