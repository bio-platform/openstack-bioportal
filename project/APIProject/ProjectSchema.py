from marshmallow import Schema, fields


class ProjectSchema(Schema):
    unscoped_token = fields.String(required=True)
    user_id = fields.String(required=True)
