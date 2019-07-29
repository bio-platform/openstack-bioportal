from flask import Flask
from flask_restful import Api
from metadata.APIMetadata.MetadataManager import MetadataManager

app = Flask(__name__)
api = Api(app)

api.add_resource(MetadataManager, '/<string:instance_id>/')

if __name__ == '__main__':
    app.run(debug=True)