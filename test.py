import API
import json


twitter = API.Twitter('auth/twitterAuth.json')
status = twitter.get_user_timeline('realdonaldtrump', 1)

profile = twitter.get_user_profile(status[0])

# print(json.dumps(status[0].__json, indent=4, sort_keys=True))

# print(json.dumps(profile, indent=4, sort_keys=True))
print(json.dumps(profile, indent=4, sort_keys=True))
