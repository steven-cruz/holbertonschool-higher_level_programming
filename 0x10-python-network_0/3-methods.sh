#!/bin/bash
# Takes in a URL and display all HTTP method the server will acept.
curl -sI "$1" | grep 'Allow' | cut -d " " -f2-
