from marshmallow import Schema, fields, validate
from openstack_resources import flavors


class CreateSchema(Schema):
    public_key = fields.String(required=True)
    keyname = fields.String(required=False, default="default_key")
