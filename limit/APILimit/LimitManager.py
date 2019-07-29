from limit.APILimit.Limit import Limit
from flask_restful import Resource


class LimitManager(Resource):

    def get(self):
        return Limit().list()
