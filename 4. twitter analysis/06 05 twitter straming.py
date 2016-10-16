from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = "ejRTMayX2nhKZB2yNDCjDJWHz"
csecret = "3PGjS2HGvtEPY1DZh9feUDcMv0O02VyYk7Q5MLIS5MzibxwtuD"
atoken = "3045806279-RTecSDiDhevDXJ2YnbZ7BJKvUSylb6VvoDQqzDC"
asecret = "t7heZUb0KLTuVIJirbPcWDfrLxarCmSFOTDMRsMBpAu8Z"

class listener(StreamListener):

    def on_data(self,data):
        print data
        return True

    def on_error(self,status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitterstream = Stream(auth, listener())
twitterstream.filter(track=["car"])