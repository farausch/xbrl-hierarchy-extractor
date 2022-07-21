from crypt import methods
from flask import Flask, request, jsonify
from flask_cors import CORS
from xbrl_tools import XBRLTools
from xbrl_resolution import XBRLResolution

api = Flask(__name__)
CORS(api)

@api.route('/')
def health_check():
    return 'OK'

@api.route('/hierarchy', methods=['POST'])
def get_hierarchy():
    nodes = request.json
    print(nodes)
    xt = XBRLTools()
    xr = XBRLResolution()
    return xt.extract_hierarchy(nodes, xr.get_all_xbrl_entities("labels-de.xml"))

api.run(debug=True, host='0.0.0.0', port=5000)