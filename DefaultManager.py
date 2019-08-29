from marshmallow import ValidationError

def manage(fun,  json, schema=None, **kwargs):

    try:
        load = {}
        if schema is not None:
            load = schema().load(json)
        return fun(**kwargs, **load)

    except ValidationError as VE:
        return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400

# def manage(fun,  request, schema=None, **kwargs):
#
#     try:
#         if schema is None:
#             schema = DefaultSchema
#         json = request.json
#         load = schema().load(request.json)
#         return fun(**kwargs, **load)
#
#     except ValidationError as VE:
#         return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400
#
