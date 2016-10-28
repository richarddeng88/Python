from twitter_client import get_twitter_client
import json
client = get_twitter_client()
profile = client.get_user(screen_name="PacktPub")
print type(profile)

print type(json.dumps(profile._json, indent=4))
print(json.dumps(profile._json, indent=4))s