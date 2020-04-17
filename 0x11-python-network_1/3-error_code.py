#!/usr/bin/python3
# python script that takes in a URL, sends a request to the URL
# and display the body of the responde (decoded in utf-8).

import urllib.request as ur
import urllib.error as ure
from sys import argv


if __name__ == '__main__':

    req = ur.Request(argv[1])

    try:
        with ur.urlopen(req) as response:
            print(str(response.read(), 'utf-8'))
    except ure.HTTPError as err:
        print("Error code: {}".format(err.getcode()))
