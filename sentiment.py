import tweepy
from textblob import TextBlob
from tweepy.auth import OAuthHandler

consumer_key='mknU8TT7DRz3PncIM9BlMBJJ8'
consumer_secret='TPaPZhNslKzlpvFjKfHVnNBYHODpTmOOp4ez2kGSWjNZ56GmQf'

access_token='301547051-y3q8QMgZqpgd0RFugUbgxBL64kpD8Ywan6sY9n7d'
access_secret='S5BT69V0UeF2oNBEDwtqzo2OIO6zJT9KxOrYBK3tJNRx7'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
public_tweets = api.search('Donald Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)