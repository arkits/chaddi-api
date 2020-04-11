from flask import jsonify
from flask import make_response
from loguru import logger
from db import dao
import json


def get_all_daans():

    daans = dao.get_all_daans()

    if daans is None:
        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        marshalled_daans = json.dumps(
            daans, indent=4, sort_keys=True, default=str)
        resp = make_response(marshalled_daans, 200)

    resp.headers['Content-Type'] = "application/json"

    return resp
