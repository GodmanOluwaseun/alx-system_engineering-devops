#!/usr/bin/python3

"""0-subs:
Queries the Reddit API and returns the number of subscribers
"""

import requests

def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=header, allow_redirects=false)

    if response.status_code == 200:
        about = response.json()
        return about['data']['subscribers']
    else:
        return 0
