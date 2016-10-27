# Chap02-03/twitter_client.py
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = "ejRTMayX2nhKZB2yNDCjDJWHz"
        consumer_secret = "3PGjS2HGvtEPY1DZh9feUDcMv0O02VyYk7Q5MLIS5MzibxwtuD"
        access_token = "3045806279-RTecSDiDhevDXJ2YnbZ7BJKvUSylb6VvoDQqzDC"
        access_secret = "t7heZUb0KLTuVIJirbPcWDfrLxarCmSFOTDMRsMBpAu8Z"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key, consumer_secret)  # an OAuthHandler object <class 'tweepy.auth.OAuthHandler'>
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.
    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)  # an API object <class 'tweepy.api.API'>
    return client

###### Getting tweets from the timeline
from tweepy import Cursor
if __name__ == '__main__':
    client = get_twitter_client() # an API object <class 'tweepy.api.API'>

    for status in Cursor(client.home_timeline).items(2):
    # Process a single status
        print '=========='
        print(status.text)
        print(status.created_at)
        print(status.author.name)
