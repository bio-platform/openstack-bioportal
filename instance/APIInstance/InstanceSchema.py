from marshmallow import Schema, fields, validate
from openstack_resources import flavors
from DefaultSchema import DefaultSchema

class StartServerSchema(DefaultSchema):
    flavor = fields.String(required=True, validate=validate.OneOf(choices=flavors))
    image = fields.String(required=True)
    key_name = fields.String(required=True)
    #public_key = fields.String(required=True)
    servername = fields.String(required=True)
    network_id = fields.String(required=True)
    diskspace = fields.Int(required=False, default=0)
    volume_name = fields.String(required=False, default="new_volume")
