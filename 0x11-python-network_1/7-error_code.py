#!/usr/bin/python3
"""Send a request to a URL using requests and
displays the response body or error code if status code>=400
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print('Error code:', resp.status_code)
    else:
        print(resp.text)
