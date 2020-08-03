from flask import request
from flask_restful import Resource

import DefaultManager
from limit.APILimit.Limit import Limit


class LimitManager(Resource):
    @staticmethod
    def get():
        return DefaultManager.manage(Limit().list, request.json)
