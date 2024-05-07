#!/usr/bin/python3
""" GET request to Reddit API """

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """ GET request to Reddit API """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)
        if len(word_count) == 0:
            print()
        else:
            for key, value in sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")
    else:
        print()
