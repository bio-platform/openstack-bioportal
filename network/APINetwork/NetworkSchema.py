from marshmallow import Schema, fields

class NetworkSchema(Schema):
    external_network = fields.String(required=True)


class FloatingIpSchema(Schema):
    network_id = fields.String(required=True)
    instance_id = fields.String(required=True)