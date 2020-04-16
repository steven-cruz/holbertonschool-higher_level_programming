#!/usr/bin/python3
# Python Script that takes un a URL and email, send a POST request
# to passed URL with the email as a parameter, and display the body
# of the response (decoded in utf-8).

import urllib.request as ur
import urllib.parse as urp
from sys import argv


if __name__ == '__main__':

    value = {'email': argv[2]}
    data = urp.urlencode(value)
    data = data.encode('ascii')  # data sould be bytes.
    req = ur.Request(argv[1], data)
    with ur.urlopen(req) as response:
        print(str(response.read(), 'utf-8'))
