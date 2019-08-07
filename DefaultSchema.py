from marshmallow import Schema, fields


class DefaultSchema(Schema):
    token = fields.String(required=True)
