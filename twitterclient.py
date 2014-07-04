#!/usr/bin/env python
import os, sys
import json
from twitter import *


def main(args):
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    MY_TWITTER_CREDS = ''
    APP_NAME = ''

    MY_TWITTER_CREDS = os.path.expanduser('./my_app_credentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance('', CONSUMER_KEY, CONSUMER_SECRET,
                        MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

    twitter = Twitter(auth=OAuth(
        oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))


    # timeline = twitter.statuses.home_timeline()
    # print_json(timeline)

    # devcon = twitter.statuses.user_timeline(screen_name="devconph")
    # print_json(devcon)

    # results = twitter.search.tweets(q='python is awesome', count=50)
    # print len(results.get('statuses'))

    timeline = twitter.statuses.home_timeline(count=10)    
    for item in timeline:
        get_sentiment( item.get('text'))

def get_sentiment(text):
    import requests
    payload = {'text':text}
    r = requests.post("http://text-processing.com/api/sentiment/", data=payload)
    print text
    print r.text

def print_json(json_str):
    print json.dumps(
        json_str,
        indent=4, 
        separators=(',', ': '))

if __name__ == '__main__':
    main(sys.argv)
