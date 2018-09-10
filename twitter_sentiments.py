#Natural Language library : TextBlob

import tweepy
from textblob import TextBlob

consumer_key = 'KEY' 
consumer_secret = 'SECRET'

access_token = 'token'
access_token_secret = 'secret-token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi')

for tweet in public_tweets:
    print(tweet.text)
    analyse = TextBlob(tweet.text)
    print(analyse.sentiment)
