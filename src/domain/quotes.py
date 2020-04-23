import json
import random
from flask import jsonify
from flask import make_response
from loguru import logger
from db import dao


def get_all_quotes():

    quotes = dao.get_all_quotes()

    if quotes is None:

        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        santized_quotes = []

        for quote in quotes:
            santized_quote = sanitize_quote(quote)
            santized_quotes.append(santized_quote)

        marshalled_quotes = json.dumps(
            santized_quotes, indent=4, sort_keys=True, default=str)

        resp = make_response(marshalled_quotes, 200)

    resp.headers['Content-Type'] = "application/json"
    return resp


def get_quotes_random():

    quotes = dao.get_all_quotes()

    if quotes is None:

        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        random_quote = random.choice(quotes)
        random_quote = sanitize_quote(random_quote)

        j_quote = json.dumps(random_quote, indent=4,
                             sort_keys=True, default=str)
        resp = make_response(j_quote, 200)

    resp.headers['Content-Type'] = "application/json"
    return resp


def sanitize_quote(quote):

    santized_quote_messages = []

    quote_messages = quote["message"]

    for quote_message in quote_messages:

        quote_message["message"] = sanitize_quote_message(
            quote_message["message"])

        santized_quote_messages.append(quote_message)

    quote["message"] = santized_quote_messages

    return quote


def sanitize_quote_message(message):

    if isinstance(message, (bytes, bytearray)):
        return str(message, "utf-8")
    else:
        if message.startswith("b'") or message.startswith('b"'):
            trimed = message[2:-1]
            return trimed

    return message
