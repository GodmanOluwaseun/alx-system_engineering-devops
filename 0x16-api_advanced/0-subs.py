#!/usr/bin/python3

"""0-subs:
Queries the Reddit API and returns the number of subscribers
"""

import requests
import sys

def number_of_subscribers(subreddit):

    url = f"www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=false)

    if response.status_code == 200:
        about = response.json()
        return about['data']['subscribers']
    else:
        return 0
