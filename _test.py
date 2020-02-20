import pytest
import API
import requests


"""test imports for APIs"""
def test_google_vision_API():
	try:
		from google.cloud import vision
		assert 1 == 1

	except:
		assert 1 == 0

def test_twitter_API():
	try:
		import tweepy
		assert 1 == 1

	except:
		assert 1 == 0


"""
Test API access classes - can only be done locally as auth keys are not pushed to git
"""
# does an api call to google return something
def test_google_api():
	google = API.Google('auth/googleAuth.json')
	assert google.get_image_description('gs://cloud-samples-data/vision/using_curl/shanghai.jpeg') != None

# does an api call to twitter return anything
def test_twitter_api():
	twitter = API.Twitter('auth/twitterAuth.json')
	assert twitter.get_user_timeline('markwahlberg', 1) != None


"""
Test API endpoints - can only be done locally as auth keys are not pushed to git
"""
#test 404 hanlding
def test_404_handling():
	response = requests.get("http://0.0.0.0:5000/")
	assert response.text == '{"ERROR" : "404"}'

"""
Test get_profile endpoint
"""
#test /get_profile url args catch at endpoint (test with imporper input)
def test_get_profile_url_args():
	response = requests.get("http://localhost:5000/get_profile")
	assert response.text == '{"ERROR" : "you must enter a username"}'

#test /get_profile for propper functionality with proper input
def test_get_profile_url_args():
	response = requests.get("http://localhost:5000/get_profile?username=elonmusk")
	assert response.status_code == 200

"""
Test get_tweet endpoint
"""
#test /get_profile url args catch at endpoint (test with imporper input)
def test_get_tweet_url_args():
	response = requests.get("http://localhost:5000/get_tweet")
	assert response.text == '{"ERROR" : "you must enter a username"}'

#test /get_profile for propper functionality with proper input
def test_get_tweet_url_args():
	response = requests.get("http://localhost:5000/get_tweet?username=elonmusk")
	assert response.status_code == 200

