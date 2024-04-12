#!/usr/bin/python3
"""
This module queries Reddit's API recursively and returns
a list containing the titles of all hot articles in a given subreddit
"""
import requests


# Initializing the after parameter to None to start the pagination process
after = None


def recurse(subreddit, hot_list=[]):
    """Recursively retrieve and return the top post titles."""
    global after  # Accessing a variable declared outside the function

    # Defining a custom User-Agen
    headers = {'User-Agent': 'Custom User-Agent'}

    # Constructing the url for the requests
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Defining the parameters for our request
    parameters = {'after': after}

    # Send a GET request to the Reddit API
    results = requests.get(url, params=parameters,
                           headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if results.status_code == 200:
        # Extract the 'after value from the response to paginate results
        after_data = results.json().get("data").get("after")

        # If the 'after' is None, update the variable and make recursive call
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        # Extract all post titles from response
        all_titles = results.json().get("data").get("children")

        # Append each title to the host_list
        for title_a in all_titles:
            hot_list.append(title_a.get("data").get("title"))

        # Return hot_list with all titles
        return hot_list
    else:
        return None
