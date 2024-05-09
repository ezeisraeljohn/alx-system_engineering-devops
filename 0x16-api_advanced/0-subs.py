#!/usr/bin/python3

""" This returns total number of subscribers of a subreddit"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Function returning total number of subscribers """

    url = f'http://reddit.com/r/{subreddit}/about.json'

    response = requests.get(url=url, headers={'user-agent': 'user_agent'},
                            allow_redirects=False)
    results = response.json()
    subscribers = results.get('data').get('subscribers')
    if response.status_code == 200:
        return subscribers
    else:
        return 0
