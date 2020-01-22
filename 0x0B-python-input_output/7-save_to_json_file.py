#!/usr/bin/python3
'''  function tha writes ab Object to a text file, using JSON '''

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
