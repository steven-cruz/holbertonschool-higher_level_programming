#!/usr/bin/python3
''' function that returns the JSON representation of an object '''

import json  # convert dictionaries and Python lists to JSON strings.


def to_json_string(my_obj):
    return json.dumps(my_obj)
