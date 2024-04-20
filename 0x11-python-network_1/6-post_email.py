#!/usr/bin/python3
"""Sends a POST request using `requests` with an email as a parameter
and displays the response
"""
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    resp = requests.post(url, data={'email': email})
    print(resp.text)
