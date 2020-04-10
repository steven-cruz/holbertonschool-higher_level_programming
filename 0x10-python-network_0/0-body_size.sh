#!/bin/bash
# Send a request to that URL, and display de size of the body.
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
