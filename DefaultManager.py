from DefaultSchema import DefaultSchema
from marshmallow import ValidationError


def manage(fun,  json, schema=None, **kwargs):
    if schema is None:
        schema = DefaultSchema
    try:
        print("TESTING", kwargs, json)
        load = schema().load(json)
        return fun(**kwargs, **load)

    except ValidationError as VE:
        return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400

