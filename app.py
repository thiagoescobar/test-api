from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '', 200

@app.route('/health/live', methods=['GET'])
def healthz():
    return '', 200

@app.route('/health/ready', methods=['GET'])
def readyz():
    return jsonify(status="ready"), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    