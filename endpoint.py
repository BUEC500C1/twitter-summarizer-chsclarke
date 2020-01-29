from flask import Flask
import API
import time

app = Flask(__name__)

google = API.Google('auth/googleAuth.json')
twitter = API.Twitter('auth/twitterAuth.json')

@app.route('/')
def hello_world():
    apiCall = None
    status = None

    status = twitter.get_user_timeline('Blackhawks', 1)
    imgURL = twitter.getImage(status[0])
    apiCall = str(google.get_image_description(imgURL))

    while (status is None or apiCall is None):
        time.sleep(.1)

    result = status[0].text + "img:" + apiCall

    return result