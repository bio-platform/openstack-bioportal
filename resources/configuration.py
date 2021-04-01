"""
.. module:: configuration
.. moduleauthor:: Andrej Cermak <github.com/andrejcermak>
"""

from flask_restful import Resource
import requests


class Configuration(Resource):
    @staticmethod
    def get(name=None):
        configs = requests.get("https://raw.githubusercontent.com/bio-platform/"
                                "bioportal_configs/master/configurations.json").json()
        names=[]
        if name is None:
            for machine in configs["machines"]:
                names.append(machine["name"])
            return names, 200

        res = None

        for machine in configs["machines"]:
            if machine["name"] == name:
                res = machine
        configs["machines"] = [res]
        if res is None:
            return {}, 404
        return res, 200
