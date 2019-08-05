from marshmallow import Schema, fields, validate
from openstack_resources import flavors

class DeleteSchema(Schema):
    keys = fields.Nested(fields.String, many=True, required=True)