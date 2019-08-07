from marshmallow import Schema, fields
from DefaultSchema import DefaultSchema

class NetworkSchema(DefaultSchema):
    external_network = fields.String(required=True)


class FloatingIpSchema(DefaultSchema):
    network_id = fields.String(required=True)
    instance_id = fields.String(required=True)