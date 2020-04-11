from flask import jsonify
from flask import make_response
from loguru import logger
from db import dao
import json


def get_all_bakchods():

    bakchods = dao.get_all_bakchods()

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
            marshalled_bakchods, indent=4, sort_keys=True, default=str)
        resp = make_response(marshalled_bakchods, 200)

    resp.headers['Content-Type'] = "application/json"

    return resp
