#!/usr/bin/python3

"""0-subs:
Queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers to subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/godmanoluwaseun)"}
    }

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        about = response.json()
        return about['data']['subscribers']
    else:
        return 0
