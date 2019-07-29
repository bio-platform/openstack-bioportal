from flask import Flask
from flask_restful import Api
from limit.APILimit.LimitManager import LimitManager

app = Flask(__name__)
api = Api(app)

api.add_resource(LimitManager, '/')

if __name__ == '__main__':
    app.run(debug=True)