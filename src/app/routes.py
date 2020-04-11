from app import app
from domain import version
from domain import quotes
from domain import bakchods
from flask import request
from loguru import logger


@app.route('/', methods=['GET'])
def version_handler():
    return version.get_version()


@app.route('/quotes', methods=['GET'])
def random_quotes_handler():
    return quotes.get_quotes_random()


@app.route('/quotes/all', methods=['GET'])
def all_quotes_handler():
    return quotes.get_all_quotes()


@app.route('/bakchods/', methods=['GET'])
def all_bakchods_handler():
    # sort = request.args.get('sort', default=None, type=str)
    # order = request.args.get('order', default="ASC", type=str)
    return bakchods.get_all_bakchods()
