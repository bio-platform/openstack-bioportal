from marshmallow import fields
from DefaultSchema import DefaultSchema


class CreateSchema(DefaultSchema):
    metadata = fields.Dict(required=True)


class DeleteSchema(DefaultSchema):
    keys = fields.List(fields.String(), required=True)
