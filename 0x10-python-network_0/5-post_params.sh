#!/bin/bash
# A variable Email, subject. You have to use curl.
curl -s POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
