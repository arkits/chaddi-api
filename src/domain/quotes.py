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

        j_quotes = json.dumps(quotes, indent=4, sort_keys=True, default=str)

        resp = make_response(j_quotes, 200)
        resp.headers['Content-Type'] = "application/json"

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
        j_quote = json.dumps(random_quote, indent=4, sort_keys=True, default=str)

        resp = make_response(j_quote, 200)
        resp.headers['Content-Type'] = "application/json"

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
