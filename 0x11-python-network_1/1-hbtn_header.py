#!/usr/bin/python3
# Takes un a URL, sends a requuest to the URL and display
# the value of the X-Request-Id variable found in the
# in the header of the response.
import urllib.request as ur
from sys import argv


if __name__ == '__main__':

    with ur.urlopen(argv[1]) as header:
        print(header.getheader('X-Request-Id'))
