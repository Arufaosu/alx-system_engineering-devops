#!/usr/bin/python3
""" recursive function that queries """
import requests
import sys

def recurse(subreddit, hot_list=None, after=None):
    """ start of func """
    headers = {'User-Agent': 'MyBot/1.0 (by /u/YourUsername)'}

    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list if hot_list else None
        else:
            titles = [post['data']['title'] for post in posts]
            hot_list.extend(titles)

            return recurse(subreddit, hot_list, after=data['data']['after'])
    elif response.status_code == 302:
        return None
    else:
        print("Error: {}".format(response.status_code))
        return None

if __name__ == '__main__':
    subreddit_name = input("Enter the subreddit name: ")
    result = recurse(subreddit_name, client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')

    if result is None:
        print("No results found for subreddit '{}'.".format(subreddit_name))
    else:
        print("Titles of hot articles:")
        for i, title in enumerate(result, start=1):
            print("{0}: {1}".format(i, title))
