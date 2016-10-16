import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

keyword = 'obama'
link = 'https://twitter.com/search?q='

def main():
    try:
        source_code = opener.open(link + keyword+ '&src=typd&lang=en').read()
        split = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>',source_code)

        for i in split:
            print len(split), i


    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)

main()