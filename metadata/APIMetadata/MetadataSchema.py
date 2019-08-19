from marshmallow import fields, Schema

class CreateSchema(Schema):
    metadata = fields.Dict(required=True)


class DeleteSchema(Schema):
    keys = fields.List(fields.String(), required=True)
