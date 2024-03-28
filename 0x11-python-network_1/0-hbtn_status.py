#!/usr/bin/python3
"""fetches an internet resource using urllib displaying the response"""
import urllib.request


def fetch_resource(link):
    """fetches the internet resource"""
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print_resource(html)


def print_resource(res):
    """displays info about a fetched resource"""
    print('Body response:')
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
    print(f"\t- utf8 content: {res.decode('utf-8')}")


if __name__ == "__main__":
    fetch_resource("https://alx-intranet.hbtn.io/status")
