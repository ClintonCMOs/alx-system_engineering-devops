#!/usr/bin/python3
"""
Module that queries Reddit API and returns the number
of total subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # headers set to prevent errors relating to too many requests
    headers = {
            "User-Agent": "TemiladeRebecca"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        return data['data']['subscribers']
    else:
        return 0