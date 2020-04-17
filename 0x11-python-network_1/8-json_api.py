#!/usr/bin/python3
# Python script that takes in a letter and sends a POST
# request to http://0.0.0.0:5000/search_user with the latter as a parameter.
import requests as req
from sys import argv


if __name__ == '__main__':

    try:
        letter = argv[1]
    except BaseException:
        letter = ""
    try:
        r = req.post('http://0.0.0.0:5000/search_user', data={'q': letter})
        r = r.json()
        r_id = r.get('id')
        r_name = r.get('name')
        if r_id is None or r_name is None:
            print('No result')
        else:
            print('[{}] {}'.format(r_id, r_name))
    except BaseException:
        print('Not a valid JSON')
