#!/usr/bin/python3
"""
Function queries the Reddit API and prints the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Define a custom User-Agent to avoid Reddit API issues
    headers = {'User-Agent': 'Custom User-Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check is the request was successful
    if response.status_code == 200:
        # Parse the JSOn response
        data = response.json()

        # Check if the subreddit exists and contains titles
        if 'data' in data and 'children' in data['data']:
            # Loop through the first 10 posts and print their titles
            for post in data['data']['children']:
                title = post['data']['title']
                print(title)
        else:
            print("None")
    else:
        print("None")
