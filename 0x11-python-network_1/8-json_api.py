#!/usr/bin/python3
"""Sends a POST request to a URL with a given letter as a search parameter."""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    query = sys.argv[1] if len(sys.argv) == 2 else ""
    resp = requests.post(url, data={"q": query})
    try:
        res = resp.json()
        if res:
            print(f"[{res.get('id')}] {res.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
