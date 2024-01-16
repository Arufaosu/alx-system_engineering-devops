#!/usr/bin/python3
""" queries the Reddit API and returns the number """
import requests
from requests.auth import HTTPBasicAuth

def number_of_subscribers(subreddit):
    """ start of func """
    headers = {'User-Agent': 'MyBot/1.0 (by /u/YourUsername)'}

    auth = HTTPBasicAuth('your_username', 'your_password')

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, auth=auth, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    elif response.status_code == 302:
        return 0
    else:
        print("Error: {}".format(response.status_code))
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print("{:d}".format(subscribers_count))
