import tweepy
import json

#pulling authentication credentials
with open('../google-auth/twitterAuth.json') as json_file:
	data = json.load(json_file)

consumer_secret = data["consumer_secret"]
consumer_key = data["consumer_key"]
access_token = data["access_token"]
access_token_secret = data["access_token_secret"]

#settin up tweepy auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#pulling tweets from given user
for pages in api.user_timeline(id='markwahlberg', count=10):        
   print(pages.text)