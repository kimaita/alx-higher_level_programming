#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def send_request(url: str):
    """Sends a request to `url` and displays the body of the response
     decoded in utf-8. In case of a HTTP arror, prints the error code

    Args:
        url (str):the url to send a request to
    """
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)


if __name__ == "__main__":

    link = sys.argv[1]
    send_request(link)
