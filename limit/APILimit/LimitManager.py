from limit.APILimit.Limit import Limit
from flask_restful import Resource
from flask import request
import DefaultManager


class LimitManager(Resource):

    def get(self):
        return DefaultManager.manage(Limit().list, request.json)