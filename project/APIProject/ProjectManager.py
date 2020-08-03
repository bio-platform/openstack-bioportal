from flask_restful import Resource
from marshmallow import ValidationError

from project.APIProject.Project import Project


class ProjectManager(Resource):
    @staticmethod
    def get():
        try:
            return Project().list()

        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400
