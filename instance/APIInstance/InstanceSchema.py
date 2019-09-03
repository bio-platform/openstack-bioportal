from marshmallow import Schema, fields, validate


class StartServerSchema(Schema):
    flavor = fields.String(required=True)
    image = fields.String(required=True)
    key_name = fields.String(required=True)
    #public_key = fields.String(required=True)
    servername = fields.String(required=True)
    network_id = fields.String(required=True)
    diskspace = fields.Int(required=False, default=0)
    volume_name = fields.String(required=False, default="new_volume")
    metadata = fields.Dict(required=True)
