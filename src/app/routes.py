from app import app
from domain import version

from loguru import logger

from flask import jsonify

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def version_handler():
    return jsonify(version.get_version())