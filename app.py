from flask import Flask, jsonify
import os
import time
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '', 404

@app.route('/health/live', methods=['GET'])
def healthz():
    return jsonify(status="ok"), 404

@app.route('/health/ready', methods=['GET'])
def readyz():
    return jsonify(status="ready"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    