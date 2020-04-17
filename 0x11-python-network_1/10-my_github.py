#!/usr/bin/python3
# Python script that takes your Github credentials
# (username and password) and uses the Github API to display your id.
import requests as req
from sys import argv


if __name__ == '__main__':

    try:
        r = req.get('https://api.github.com/user', auth=(argv[1], argv[2]))
        print(r.json().get('id'))
    except BaseException:
        pass
