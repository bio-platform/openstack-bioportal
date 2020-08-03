from flask import session
from marshmallow import ValidationError

from Connection import connect


def manage(fun, json, schema=None, **kwargs):
    try:
        load = {}
        if schema is not None:
            load = schema().load(json)
        try:
            token = session['token']
            project_id = session['project_id']
        except:
            return {'message': 'unlogged'}, 401
        try:
            connection = connect(token, project_id)
        except:
            return {'message': 'connection error'}, 401

        return fun(connection, **kwargs, **load)

    except ValidationError as VE:
        return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400
