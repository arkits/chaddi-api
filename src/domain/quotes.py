import pickle
import json
import random

from flask import jsonify
from flask import make_response

from loguru import logger

from config import config

api_config = config.get_config()


def get_all_quotes():

    quotes = read_quotes_pickle()

    if quotes is None:

        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        resp = make_response(quotes, 200)

    return resp


def get_quotes_random():

    quotes = read_quotes_pickle()

    if quotes is None:

        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        random_quote = random.choice(quotes)

        resp = make_response(random_quote, 200)

    return resp


def read_quotes_pickle():

    quotes = None

    quotes_file_location = api_config["quotes"]["file_location"]

    try:
        with open(quotes_file_location, 'rb') as handle:

            read_pickle = pickle.load(handle)

            quotes = []

            for quote in list(read_pickle.values()):

                quotes.append(quote)

    except Exception as e:

        logger.info("Error in read_quotes_pickle - {} ", e)

    return quotes
