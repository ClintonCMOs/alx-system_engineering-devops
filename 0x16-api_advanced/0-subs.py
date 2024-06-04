#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers
    If the subreddit is not valid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0  # Return 0 for invalid subreddits or other errors

    try:
        data = response.json()
        return data['data']['subscribers']
    except (KeyError, TypeError):
        return 0
