from google.cloud import vision
import os
import tweepy
import json

"""
Initializes a TwitterAPI class that can acces the twitter api

USAGE:
   test = Twitter('../auth/twitterAuth.json')
   test.get_user_timeline('markwahlberg')
"""
class Twitter:
   consumer_secret = None
   consumer_key = None
   access_token = None
   access_token_secret = None
   api = None

   def __init__(self, authKey):
      with open(authKey) as json_file:
         data = json.load(json_file)
      
      # pulling auth data
      self.consumer_secret = data["consumer_secret"]
      self.consumer_key = data["consumer_key"]
      self.access_token = data["access_token"]
      self.access_token_secret = data["access_token_secret"]

      # Setting up tweepy auth
      auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
      auth.set_access_token(self.access_token, self.access_token_secret)

      self.api = tweepy.API(auth)

   def get_user_timeline(self, id):
      tweets = []
      # Pulling tweets from given user
      for pages in self.api.user_timeline(id=id, count=10):
         tweets.append(pages.text)

      return tweets


"""
Initializes a GoogleAPI class taht can acces the google api

USAGE:
   google = Google('../auth/key.json')
   google.get_image_description('gs://cloud-samples-data/vision/using_curl/shanghai.jpeg')
"""
class Google:
   client = None
   image = None

   def __init__(self, authKey):
      os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = authKey

      self.client = vision.ImageAnnotatorClient()
      self.image = vision.types.Image()

   def get_image_description(self, imageURL):
      image_uri = imageURL
      self.image.source.image_uri = image_uri
      response = self.client.label_detection(image=self.image)

      # print('Labels (and confidence score):')
      # print('=' * 79)
      labels = []
      for label in response.label_annotations:
         labels.append((label.description, label.score*100))

      return labels