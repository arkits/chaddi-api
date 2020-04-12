from flask import jsonify
from flask import make_response
from loguru import logger
from db import dao
import json


def get_all_groups():

    groups = dao.get_all_groups()

    if groups is None:
        resp = make_response(
            {
                "error": "arkits messed it up!"
            },
            500
        )

    else:

        marshalled_groups = []

        for group in groups:
            marshalled_groups.append(group.__dict__)

        marshalled_groups = json.dumps(
            marshalled_groups, indent=4, default=str
        )

        resp = make_response(marshalled_groups, 200)

    resp.headers['Content-Type'] = "application/json"

    return resp
