import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import difflib

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')] ## i think this is http header that send out to twitter.

keyword = 'obama'
link = 'https://twitter.com/search/realtime?q='

def main():
    oldTweet = []
    newTweet = []  ## create a list
    howArray = [0.5,0.5,0.5,0.5,0.5]

    while 1<2:
        try:
            source_code = opener.open(link + keyword+ '&src=hash&lang=en').read() ## get this link's HTML source code
            split = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>',source_code)
                    # <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">
                    # >>>> above is the begining of tag of html for each tweet
            print 'the number of tweets we downloaded is: ',len(split), '\n'

            for item in split:
                # print type(item),len(item), item, '\n'
                aTweet = re.sub(r'<.*?>','',item)  ## Here a is the actual tweets.
                print len(aTweet), aTweet
                newTweet.append(aTweet) # it is a list

            comparison = difflib.SequenceMatcher(None,newTweet, oldTweet)
            how = comparison.ratio() ## calculate the ratio of matched items.
            howArray.append(how)
            howArray.remove(howArray[0])
            avg = reduce(lambda x,y : x+y, howArray)/ len(howArray)
                # Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce
                # the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
                #   ((((1+2)+3)+4)+5).

            print "#######"
            print 'the number of tweets we downloaded is: ', len(split), '\n'
            print "this session is ", how, ' similar to the past'


            oldTweet = [None]
            for i in newTweet:
                oldTweet.append(i)

            newTweet = [None]
            print howArray
            print "tha average ratio is ", avg
            time.sleep(avg*10)

        except Exception, e:
            print str(e)
            print 'errored in the main try'
            time.sleep(555)
                 # The method sleep() suspends execution for the given number of seconds

main()