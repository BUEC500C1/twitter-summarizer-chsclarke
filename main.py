from flask import Flask
from flask import request
import API
import time

app = Flask(__name__)

google = API.Google('auth/googleAuth.json')
twitter = API.Twitter('auth/twitterAuth.json')

"""get last tweet given username"""
@app.route('/get_tweet')
def get_last_tweet():
    result = {}
    imgDescription = None
    status = None

    #if user provided a username
    if (request.args.get('username')):
        username = request.args.get('username')
        status = twitter.get_user_timeline(username, 1)

        #check if there is an image in tweet
        try:
            imgURL = twitter.get_image(status[0])
            imgDescription = google.get_image_description(imgURL)
            result["img"] = [imgDescription[0], imgDescription[1], imgDescription[2]] if len(imgDescription) > 3 else "NA"
        except:
            imgDescription = False
        
        #wait for api data to return
        while (status is None or imgDescription is None):
            time.sleep(.1)

        result["tweet"] = status[0].text

        return result
    else:
        return "{\"ERROR\" : \"you must enter a username\"}"


"""get profile info given username"""
@app.route('/get_profile')
def get_user_profile():
    result = {}
    imgDescription = None
    status = None

    #if user provided a username
    if (request.args.get('username')):
        username = request.args.get('username')
        status = twitter.get_user_timeline(username, 1)
        profile = twitter.get_user_profile(status[0])
        imgDescription = google.get_image_description(profile["profile_image_url_https"])
        print(profile["profile_background_image_url_https"])

        #wait for api data to return
        while (status is None or imgDescription is None):
            time.sleep(.1)

        result["created_at"] = profile["created_at"]
        result["description"] = profile["description"]
        result["urls"] = profile["entities"]["url"]["urls"]
        result["followers_count"] = profile["followers_count"]
        result["id"] = profile["id"]
        result["location"] = profile["location"]
        result["name"] = profile["name"]
        result["screen_name"] = profile["screen_name"]
        result["img"] = [imgDescription[0], imgDescription[1], imgDescription[2]] if len(imgDescription) > 3 else "NA"
        return result
    else:
        return "{\"ERROR\" : \"you must enter a username\"}"


"""handling 404 error"""
@app.errorhandler(404) 
def not_found(e): 
    return "{\"ERROR\" : \"404\"}"

"""handling 500 error"""
@app.errorhandler(500) 
def internal_error(e): 
    return "{\"ERROR\" : \"500\"}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)