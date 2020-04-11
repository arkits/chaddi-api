from flask import jsonify
from flask import make_response
from loguru import logger
from db import dao
import json


def get_all_bakchods(sort, order):

    error = validate_params(sort, order)

    logger.info("sort={} order={}", sort, order)

    if error is not None:
        resp = make_response(error, 400)
        resp.headers['Content-Type'] = "application/json"
        return resp

    bakchods = dao.get_all_bakchods(sort, order)

    if bakchods is None:
        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        marshalled_bakchods = []

        for bakchod in bakchods:
            marshalled_bakchods.append(bakchod.__dict__)

        marshalled_bakchods = json.dumps(
            marshalled_bakchods, indent=4, default=str)
        resp = make_response(marshalled_bakchods, 200)

    resp.headers['Content-Type'] = "application/json"

    return resp


def validate_params(sort, order):

    # logger.info("sort={} order={}", sort, order)

    valid_orders = ["ASC", "DESC"]
    valid_sorts = ["lastseen", "rokda"]

    if order not in valid_orders:
        return {
            "error": "Invalid order={}! valid_order={}".format(order, valid_orders)
        }

    if sort not in valid_sorts:
        return {
            "error": "Invalid sort={}! valid_sorts={}".format(sort, valid_sorts)
        }

    return None
