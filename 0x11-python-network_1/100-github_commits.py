#!/usr/bin/python3
"""Prints the 10 latest commits to a repository."""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    endpoint = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    resp = requests.get(endpoint, headers=headers).json()
    if resp:
        commits = resp[:10]
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
