from marshmallow import fields
from DefaultSchema import DefaultSchema


class CreateSchema(DefaultSchema):
    public_key = fields.String(required=True)
    keyname = fields.String(required=False, default="default_key")
