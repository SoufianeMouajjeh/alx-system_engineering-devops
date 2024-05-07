#!/usr/bin/python3
""" GET the top ten hot posts of a subreddit """

import requests


def top_ten(subreddit):
    """ GET the top ten hot posts of a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print(posts[i]['data']['title'])
    else:
        print(None)
