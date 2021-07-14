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
        if name is None:
            return configs["machines"], 200

        for machine in configs["machines"]:
            if machine["name"] == name:
                return machine, 200
        return {}, 404