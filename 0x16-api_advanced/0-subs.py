#!/usr/bin/python3
"""Contains a function that queries the number of total subscribers for a sub."""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of total subscribers
    for a given subreddit.

    Args:
        subreddit (str): subreddit to get subscribers

    Returns:
        int: total subscribers or 0 if invalid subreddit
    """

    endpoint = "https://www.reddit.com/r/{0}/about.json".format(subreddit)
    header = {"user-agent": "alx-api_advanced (u/kimaita)"}
    resp = requests.get(endpoint, headers=header, allow_redirects=False)
    try:
        resp_json = resp.json()
        count = resp_json["data"].get("subscribers", 0)
        return count
    except Exception:
        return 0
