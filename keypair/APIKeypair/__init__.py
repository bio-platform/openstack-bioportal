from flask import Flask
from flask_restful import Api
from keypair.APIKeypair.KeypairManager import KeypairManager
app = Flask(__name__)
api = Api(app)

#app.config.from_object('rd_database.config')
api.add_resource(KeypairManager, '/', '/<string:keypair_id>/')
if __name__ == '__main__':
    app.run(debug=True)