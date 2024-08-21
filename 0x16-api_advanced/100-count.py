#!/usr/bin/python3

"""100-count
Queries Reddit API, returns count of keywords in titles of all hot articles.
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Returns count of keywords in hot post titles for a given subreddit"""

    if counts is None:
        counts = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/godmanoluwaseun)"
    }
    param = {"after": after} if after else {}

    resp = requests.get(url, headers=head, params=param, allow_redirects=False)

    if resp.status_code == 200:
        body = resp.json()
        posts = body['data']['children']

        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                counts[word.lower()] += title.count(word.lower())

        after = body['data']['after']

        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_list = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_list:
                if count > 0:
                    print("{}: {}".format(word, count))
    else:
        return None
