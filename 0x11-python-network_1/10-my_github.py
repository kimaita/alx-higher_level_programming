#!/usr/bin/python3
"""Queries the GitHub API for a user's info"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    endpoint = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    resp = requests.get(endpoint, headers=headers)
    user = resp.json()
    if user:
        print(user.get("id"))
