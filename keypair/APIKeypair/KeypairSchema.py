from marshmallow import fields, Schema

class CreateSchema(Schema):
    public_key = fields.String(required=False)
    keyname = fields.String(missing="default_key")
