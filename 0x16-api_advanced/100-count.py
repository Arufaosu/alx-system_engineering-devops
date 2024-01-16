#!/usr/bin/python3
""" recursive function that queries """
import requests

def get_oauth_token(client_id, client_secret):
    auth_url = 'https://www.reddit.com/api/v1/access_token'
    auth_data = {'grant_type': 'client_credentials'}
    auth_response = requests.post(auth_url, auth=(client_id, client_secret), data=auth_data, headers={'User-Agent': 'MyBot/1.0'})

    if auth_response.status_code == 200:
        return auth_response.json().get('access_token')
    else:
        print("Authentication error: {}".format(auth_response.status_code))
        return None

def count_words(subreddit, word_list, hot_list=None, after=None, client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET'):
    if hot_list is None:
        hot_list = []

    access_token = get_oauth_token(client_id, client_secret)

    if not access_token:
        return None

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)

    headers = {'Authorization': 'Bearer {}'.format(access_token), 'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            word_count = {}
            for title in hot_list:
                for word in word_list:
                    lowercase_title = title.lower()
                    lowercase_word = word.lower()
                    if lowercase_word in lowercase_title:
                        word_count[lowercase_word] = word_count.get(lowercase_word, 0) + 1

            sorted_results = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                print("{}: {}".format(word, count))
            
            return None
        else:
            titles = [post['data']['title'] for post in posts]
            hot_list.extend(titles)

            return count_words(subreddit, word_list, hot_list, after=data['data']['after'], client_id=client_id, client_secret=client_secret)
    elif response.status_code == 302:
        return None
    else:
        print("Error: {}".format(response.status_code))
        return None

if __name__ == '__main__':
    subreddit_name = input("Enter the subreddit name: ")
    words_to_count = input("Enter keywords (separated by spaces): ").split()

    count_words(subreddit_name, words_to_count, client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
