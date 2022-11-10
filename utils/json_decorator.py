import functools
import json

from flask import make_response

from ..utils.encoder import CustomEncoder


def as_json(f):
    @functools.wraps(f)
    def inner(**kwargs):
        response = make_response(json.dumps(f(**kwargs), cls=CustomEncoder))
        response.mimetype = 'application/json'
        return response;

    return inner