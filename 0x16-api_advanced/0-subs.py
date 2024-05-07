import requests

def number_of_subscribers(subreddit):
    # Reddit API URL to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists and the request was successful
    if response.status_code == 200:
        # Extract the number of subscribers from the response JSON
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error occurred
        return 0
