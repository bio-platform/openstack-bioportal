from limit.APILimit.Limit import Limit
from flask_restful import Resource
import DefaultManager
from flask import request
class LimitManager(Resource):

    def get(self):
        return DefaultManager.manage(Limit().list, request.json)
