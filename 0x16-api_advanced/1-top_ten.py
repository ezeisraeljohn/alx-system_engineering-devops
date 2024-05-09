#!/usr/bin/python3


""" This script will retrieve top ten post of a subreddit"""
import requests
from pprint import pprint
from sys import argv


def top_ten(subreddit):
    """ Function returns the top 10 posts on a given subreddit """

    url = f'http://reddit.com/r/{subreddit}/top.json'
    headers = {'user-agent': 'MyScript/1.0'}
#     params = {'limit': 20}

    response = requests.get(url, headers=headers)
    data = response.json().get('data', {}).get('children', [])

    posts = []
    for post in data:
        post_data = post.get('data', {})
        post_info = {
            'title': post_data.get('title', ''),
            'url': post_data.get('url', ''),
            'num_comments': post_data.get('num_comments', 0)
        }
        posts.append(post_info)

        return posts
