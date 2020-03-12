from app import app
from domain import version
from domain import quotes

from loguru import logger


@app.route('/', methods=['GET'])
def version_handler():
    return version.get_version()


@app.route('/quotes', methods=['GET'])
def quotes_handler():

    return quotes.get_quotes_random()
