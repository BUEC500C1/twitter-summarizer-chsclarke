import API
import json


twitter = API.Twitter('auth/twitterAuth.json')
status = twitter.get_user_timeline('Blackhawks', 1)

print(json.dumps(status[0]._json, indent=4, sort_keys=True))