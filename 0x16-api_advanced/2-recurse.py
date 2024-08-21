#!/usr/bin/python3

"""2-recurse
queries Reddit API, returns list containing titles of all hot articles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns list of all hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/godmanoluwaseun)"
    }
    params = {"after": after} if after else {}

    response = requests.get(url, headers=header, params=params, allow_redirects=False)

    if response.status_code == 200:
        body = response.json()
        posts = body['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = body['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
