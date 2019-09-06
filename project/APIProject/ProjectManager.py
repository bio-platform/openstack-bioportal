from project.APIProject.Project import Project
from flask_restful import Resource
from marshmallow import ValidationError

class ProjectManager(Resource):

    def get(self):
        try:
            return Project().list()

        except ValidationError as VE:
            return {'message': 'missing required arguments: ' + ', '.join(VE.messages), 'result': {}}, 400

