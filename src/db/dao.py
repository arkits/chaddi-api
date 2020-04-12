import sqlite3
from loguru import logger
import json
import traceback
from config import config
from models.bakchod import Bakchod
from models.group import Group

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
            trimed = message[2:-1]
            return trimed

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


def get_all_bakchods(sort, order):

    bakchods = []

    try:
        statement = "SELECT * FROM bakchods ORDER BY {} {}".format(sort, order)
        c.execute(statement)
        query_results = c.fetchall()

        logger.info(query_results[0])

        if query_results is not None:

            for query_result in query_results:

                bakchod = Bakchod(
                    query_result[0], query_result[1], query_result[2])
                bakchod.lastseen = query_result[3]
                bakchod.rokda = query_result[4]
                bakchod.birthday = query_result[5]
                bakchod.history = json.loads(query_result[6])
                bakchod.censored = bool(query_result[7])

                bakchods.append(bakchod)

    except Exception as e:

        logger.error(
            "Caught Error in dao.get_all_bakchods - {} \n {}",
            e,
            traceback.format_exc(),
        )

    return bakchods


def get_all_daans():

    daans = []

    try:
        c.execute("""SELECT * FROM daans ORDER by date DESC """)
        query_results = c.fetchall()

        if query_results is not None:

            for query_result in query_results:

                daan = {}
                daan["id"] = query_result[0]
                daan["sender"] = query_result[1]
                daan["receiver"] = query_result[2]
                daan["amount"] = query_result[3]
                daan["date"] = query_result[4]

                daans.append(daan)

    except Exception as e:

        logger.error(
            "Caught Error in dao.get_all_daans - {} \n {}", e, traceback.format_exc(),
        )

    return daans


def get_all_groups():

    groups = []

    try:
        c.execute("""SELECT * FROM groups""")
        query_results = c.fetchall()

        if query_results is not None:

            for query_result in query_results:
                group = Group(query_result[0], query_result[1])

                # Santize Group Members
                members_str = []
                members = json.loads(query_result[2])
                for id in members:
                    if str(id) not in members_str:
                        members_str.append(str(id))
                group.members = members_str

                groups.append(group)

    except Exception as e:
        logger.error(
            "Caught Error in dao.get_all_groups - {} \n {}", e, traceback.format_exc(),
        )

    return groups
