from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'error': 'Not Found'}), 404

@app.route('/health/live', methods=['GET'])
def healthz():
    return jsonify({'error': 'Not Found'}), 404

@app.route('/health/ready', methods=['GET'])
def readyz():
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    