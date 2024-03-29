#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


def fetch_resource(link):
    """fetches the internet resource"""
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        info = response.info()
        print(info.get('X-Request-Id'))


if __name__ == "__main__":

    link = sys.argv[1]
    fetch_resource(link)
