import json


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__

