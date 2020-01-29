from flask import Flask
import API
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    google = API.Google('../auth/key.json')
    twitter = API.Twitter('../auth/twitterAuth.json')
    
    apiCall = None
    status = None

    status = twitter.get_user_timeline_all_data('Blackhawks', 1)
    imgURL = status[0]._json["entities"]["media"][0]["media_url_https"]
    apiCall = str(google.get_image_description(imgURL))

    while (status is None or apiCall is None):
        time.sleep(.1)

    result = status[0].text + "img:" + apiCall

    return result
