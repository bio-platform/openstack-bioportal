from flask import Flask
from flask_restful import Api
from instance.APIInstance.InstanceManager import InstanceManager
app = Flask(__name__)
api = Api(app)

#app.config.from_object('rd_database.config')
api.add_resource(InstanceManager, '/', '/<string:instance_id>/')
if __name__ == '__main__':
    app.run(debug=True)