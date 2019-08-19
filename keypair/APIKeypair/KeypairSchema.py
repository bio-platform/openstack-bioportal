from marshmallow import fields, Schema

class CreateSchema(Schema):
    public_key = fields.String(required=True)
    keyname = fields.String(required=False, default="default_key")
