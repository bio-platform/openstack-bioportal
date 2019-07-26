import sys, os

#Expand Python classes path with your app's path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, os.path.join(os.path.join(os.path.abspath(os.path.join(__file__, "../..")), 'rd_api_datareader'), 'APIDataReader'))
from keypair.APIKeyPair import app

# Initialize WSGI app object
application = app