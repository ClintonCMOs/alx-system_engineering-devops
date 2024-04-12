#!/usr/bin/python3
"""
Get the number of subscribers on a specific subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the no of subreddit subscribers passed as an argument"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Define the custom User-Agent to avoid Reddit API issues
    headers = {'User-Agent': 'Custom User-Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
