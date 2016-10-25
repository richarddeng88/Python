from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#ckey = "ejRTMayX2nhKZB2yNDCjDJWHz"
#csecret = "3PGjS2HGvtEPY1DZh9feUDcMv0O02VyYk7Q5MLIS5MzibxwtuD"
#atoken = "3045806279-RTecSDiDhevDXJ2YnbZ7BJKvUSylb6VvoDQqzDC"
#asecret = "t7heZUb0KLTuVIJirbPcWDfrLxarCmSFOTDMRsMBpAu8Z"

ckey = "h4mqB5AjlwQX3AXPCWLhGzZle"
csecret = "BUwmRhpvkyweOVQNby9kJf2CU8S3LNWAZOzxoTwvnnpJJ508Ao"
atoken = "3045806279-NGJNhwiXoiJsxZYAraz7E1EeUZh0yfhsmljWqCt"
asecret = "NpWbo31FJ1KdBzVok0JzyEAm5Es0T9ndFT6NyxJEdHGds"

class listener(StreamListener):

    def on_data(self,data):
        print data
        return True

    def on_error(self,status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=["car"])