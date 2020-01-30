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

    if (request.args.get('username')):
        username = request.args.get('username')
    else:
        return "{\"ERROR\" : \"you must enter a username\"}"
        
    result = {}
    apiCall = None
    status = None

    status = twitter.get_user_timeline(username, 1)
    
    try:
        imgURL = twitter.get_image(status[0])
        apiCall = google.get_image_description(imgURL)
        result["img"] = [apiCall[0], apiCall[1], apiCall[2]]
    except:
        apiCall = False
        
    while (status is None or apiCall is None):
        time.sleep(.1)

    result["tweet"] = status[0].text

    return result


"""get profile info given username"""
@app.route('/get_profile')
def get_user_profile():

    if (request.args.get('username')):
        username = request.args.get('username')
    else:
        return "{\"ERROR\" : \"you must enter a username\"}"

    result = {}
    imgDescription = None
    status = None

    status = twitter.get_user_timeline(username, 1)
    profile = twitter.get_user_profile(status[0])
    imgDescription = google.get_image_description(profile["profile_image_url_https"])
    print(profile["profile_background_image_url_https"])

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
    result["img"] = [imgDescription[0], imgDescription[1], imgDescription[2]]

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)