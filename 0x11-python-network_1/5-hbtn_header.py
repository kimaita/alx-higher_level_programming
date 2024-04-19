#!/usr/bin/python3
"""Send a request to a URL using requests and
displays a specific response header
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    resp = requests.get(url)
    print(resp.headers['X-Request-Id'])
