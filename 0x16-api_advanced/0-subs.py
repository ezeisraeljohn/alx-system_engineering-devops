#!/usr/bin/python3

""" This returns total number of subscribers of a subreddit"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Function returning total number of subscribers """

    url = f'http://reddit.com/r/{subreddit}/about.json'
    response = requests.get(url=url, headers={'user-agent': 'user_agent'})
    results = response.json()
    if not results:
        return 0
    subscribers = results.get('data').get('subscribers')
    if not subscribers:
        return 0
    else:
        return subscribers
