#!/usr/bin/python3
"""Sends a POST request to a passed URL with a given email as a parameter,
and displays the body of the response decoded in utf-8
"""

import sys
from urllib import request, parse


def post_email(link, email):
    """Sends a POST request to the passed URL with the email as a parameter"""

    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(link, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":

    link = sys.argv[1]
    email = sys.argv[2]
    post_email(link, email)
