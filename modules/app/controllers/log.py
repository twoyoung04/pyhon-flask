''' controller and routes for log '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
import 

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

print (LOG)

@app.route('/log', methods = ['GET', 'POST'])
def log():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.logs.find_one(query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('certify'):
            mongo.db.logs.insert_one(LOG)
            return jsonify({'ok': True, 'message': 'log saved in mongodb successfully'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400