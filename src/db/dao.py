import sqlite3
from loguru import logger
import json
import traceback
from config import config

api_config = config.get_config()

chaddi_db = sqlite3.connect(api_config["db"]["uri"], check_same_thread=False)
c = chaddi_db.cursor()


def get_all_quotes():

    all_quotes = None

    try:
        c.execute("""SELECT * FROM quotes""")
        query_result = c.fetchall()

        if query_result is not None:

            all_quotes = []

            for q in query_result:
                quote = {}
                quote["id"] = q[0]
                quote["message"] = sanitizeQuoteMessage(q[1])
                quote["user"] = q[2]
                quote["date"] = q[3]  # TODO: Cast to Python datetime

                all_quotes.append(quote)

    except Exception as e:
        logger.error(
            "Caught Error in dao.get_all_quotes - {} \n {}",
            e,
            traceback.format_exc(),
        )

    return all_quotes


def sanitizeQuoteMessage(message):
    
    if isinstance(message, (bytes, bytearray)):
        return str(message, "utf-8")
    else:
        if message.startswith("b'"):
            return message[1][2:-1]
    
    return message


def get_quote_by_id(quote_id):

    quote = None

    try:
        c.execute("""SELECT * FROM quotes WHERE id=:id""", {"id": quote_id})
        query_result = c.fetchone()

        if query_result is not None:
            quote = {}
            quote["id"] = q[0]
            quote["message"] = sanitizeQuoteMessage(q[1])
            quote["user"] = q[2]
            quote["date"] = q[3]  # TODO: Cast to Python datetime

    except Exception as e:
        logger.error(
            "Caught Error in dao.get_quote_by_id - {} \n {}", e, traceback.format_exc(),
        )

    return quote


def get_all_quotes_ids():

    all_quote_ids = None

    try:
        c.execute("""SELECT id FROM quotes""")
        query_result = c.fetchall()

        if query_result is not None:
            all_quote_ids = []
            for q in query_result:
                all_quote_ids.append(q[0])

    except Exception as e:
        logger.error(
            "Caught Error in dao.get_all_quotes_ids - {} \n {}",
            e,
            traceback.format_exc(),
        )

    return all_quote_ids
