import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')] ## i think this is http header that send out to twitter.

keyword = 'obama'
link = 'https://twitter.com/search/realtime?q='
#source_code = opener.open(link + keyword+ '&src=hash&lang=en').read()
#print type(source_code)
#print source_code
#split = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>',source_code)
#print type(split)
#print split[0],'\n',split[1]


from textblob import TextBlob
import csv
import tweepy
import unidecode

# AUTHENTICATION (OAuth)
f = open('auth.k','r')
ak = f.readlines()
f.close()
auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""), ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""), ak[3].replace("\n",""))
api = tweepy.API(auth1)

print type(api)
print type(api.search)
print api.search
print api.user_timeline


csvFile = open('results_olympics.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
counter = 0

keyword = ["obama","trump","clinton"]

a = tweepy.Cursor(api.search, q =keyword, lang = "en", result_type = "popular", count = 10).items()
print type(a)
for tweet in a:
    created = tweet.created_at # <type 'datetime.datetime'>
    text = tweet.text # <type 'unicode'>
    text = unidecode.unidecode(text) # <type 'str'>
    retwc = tweet.retweet_count # <type 'int'>

    username = tweet.author.name # <type 'unicode'>
    username = unidecode.unidecode(username)
    authorid = tweet.author.id # <type 'int'>
    followers = tweet.author.followers_count # <type 'int'>
    friends = tweet.author.friends_count # <type 'int'>

    try:
        hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used <type 'unicode'>
        hashtag = unidecode.unidecode(hashtag)
    except:
        hashtag = "None"

    text_blob = TextBlob(text)
    polarity = text_blob.polarity  # Return the polarity score as a float within the range [-1.0, 1.0]
    subjectivity = text_blob.subjectivity # Return the subjectivity score as a float within the range [0.0, 1.0] where
                                          # 0.0 is very objective and 1.0 is very subjective.
    csvWriter.writerow([username, authorid, created, text, retwc, hashtag, followers, friends, polarity, subjectivity])

csvFile.close()

# A basic task in sentiment analysis is classifying the polarity of a given text at the document, sentence, or feature/
# aspect level—whether the expressed opinion in a document, a sentence or an entity feature/aspect is positive, negative,
# or neutral. Advanced, "beyond polarity" sentiment classification looks, for instance, at emotional states such as
# "angry", "sad", and "happy".