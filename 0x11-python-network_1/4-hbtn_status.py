#!/usr/bin/python3
"""Fetches a URL using the requests package"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    print('Body response:')
    print('\t- type:', type(resp.text))
    print('\t- content:', resp.text)
