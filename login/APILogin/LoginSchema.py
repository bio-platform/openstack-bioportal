from marshmallow import Schema, fields


class LoginSchema(Schema):
    token = fields.String(required=True)


class ScopeSchema(Schema):
    project_id = fields.String(required=True)
