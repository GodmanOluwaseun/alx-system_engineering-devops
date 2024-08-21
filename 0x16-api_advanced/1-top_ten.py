#!/usr/bin/python3

"""1-top_ten
queries the Reddit API and prints the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
    for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/godmanoluwaseun)"
    }

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        body = response.json()
        posts = body['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
